from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserAccountManager(BaseUserManager):
    def create_user(self, email,name,password):
        if not email:
            raise ValueError("User Must have a valid email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name= name)

        user.set_password()
        user.save()

        return user

def create_super(self, email,name,password):
    user = self.create_user(email,name,password)

    user.is_superuser = True
    user.is_staff = True

    user.save()

    return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=30)
    name = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    USERNAME_FIELDS = ["name"]

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email

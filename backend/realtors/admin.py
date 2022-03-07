from django.contrib import admin

from backend.realtors.models import Realtor
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "data_hired")
    list_display_links = ("id", "name")
    search_fields = ("name", )
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
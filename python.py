
class Parent1:
    def __init__(self, string):
        self.string = string

    def show_parent(self):
        return self.string

class Parent2:
    def __init__(self,string2):
        self.string2 = string2

    def show_parent2(self):
        return self.string2


class Derived(Parent1, Parent2):
    # def __init__(self, string):
    def __init__(self,string3):
        self.string3 = string3
        # super().__init__(string)
        def show__derived(self):
            return self.string3
d1 = Derived("ajay")
d1.show_parent("ajay")

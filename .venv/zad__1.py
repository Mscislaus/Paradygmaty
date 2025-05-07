class User:
    def __init__(self, name, surname, isActive=True):
        self.name = name
        self.surname = surname
        self.isActive = isActive

    def print(self):
        print(f"Name: {self.name}, Surname: {self.surname}, Active: {self.isActive}")

    def setActive(self, active):
        self.isActive = active

u1 = User("Anna", "Nowak", True)
u1.print()
u1.setActive(False)
u1.print()

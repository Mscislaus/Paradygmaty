class Book:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def print_users(self):
        print("Wszyscy użytkownicy w książce:")
        for user in self.users:
            user.print()

    def print_active_users(self):
        print("Aktywni użytkownicy w książce:")
        for user in self.users:
            if user.isActive:
                user.print()

    def find_by_name(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def get_count(self):
        print(f"Liczba użytkowników: {len(self.users)}")

b = Book()
u1 = User("Anna", "Nowak")
u2 = User("Piotr", "Kowalski", False)
u3 = User("Anna", "Zielińska")

b.add_user(u1)
b.add_user(u2)
b.add_user(u3)

b.print_users()
b.print_active_users()
znaleziony = b.find_by_name("Anna")
if znaleziony:
    print("Znaleziono użytkownika:")
    znaleziony.print()
b.get_count()

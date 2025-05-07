class Osoba:
    def __init__(self, imie, nazwisko):
        self._imie = imie
        self._nazwisko = nazwisko

    def imie(self):
        print(f"Imię: {self._imie}")

    def nazwisko(self):
        print(f"Nazwisko: {self._nazwisko}")

    def __str__(self):
        return f"{self._imie} {self._nazwisko}"

os = Osoba("Katarzyna", "Wiśniewska")
os.imie()
os.nazwisko()
print(os)

class Osoba:
    def __init__(self, imie, ojciec=None):
        self.imie = imie
        self.ojciec = ojciec

def znajdz_dziadka(wnuk):
    if wnuk.ojciec and wnuk.ojciec.ojciec:
        return wnuk.ojciec.ojciec
    else:
        return None

dziadek = Osoba("Jan")
ojciec = Osoba("Marek", ojciec=dziadek)
wnuk = Osoba("Tomek", ojciec=ojciec)

dziadek_znaleziony = znajdz_dziadka(wnuk)
if dziadek_znaleziony:
    print("Dziadek to:", dziadek_znaleziony.imie)
else:
    print("Brak dziadka w drzewie.")

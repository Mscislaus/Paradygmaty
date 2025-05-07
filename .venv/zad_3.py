dzienniczek = {}

def dodaj_ocene(przedmiot, ocena):
    if przedmiot not in dzienniczek:
        dzienniczek[przedmiot] = []
    dzienniczek[przedmiot].append(ocena)

def wyswietl_oceny(przedmiot):
    if przedmiot in dzienniczek:
        print(f"Ocen(y) z {przedmiot}: {dzienniczek[przedmiot]}")
    else:
        print("Brak ocen z tego przedmiotu.")

def srednia_ocen(przedmiot):
    if przedmiot in dzienniczek and dzienniczek[przedmiot]:
        srednia = sum(dzienniczek[przedmiot]) / len(dzienniczek[przedmiot])
        print(f"Średnia ocen z {przedmiot}: {srednia:.2f}")
    else:
        print("Brak ocen, nie można obliczyć średniej.")

dodaj_ocene("matematyka", 4)
dodaj_ocene("matematyka", 5)
dodaj_ocene("polski", 3)
wyswietl_oceny("matematyka")
srednia_ocen("matematyka")

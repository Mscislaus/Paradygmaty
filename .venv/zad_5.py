import random

tablica = [random.randint(1, 100) for _ in range(20)]
print("Oryginalna tablica:", tablica)

tablica.sort()
print("Posortowana tablica:", tablica)

suma = sum(tablica)
srednia = suma / len(tablica)

print(f"Suma: {suma}")
print(f"Średnia: {srednia:.2f}")
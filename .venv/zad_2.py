def silnia(n):
    if n < 0:
        return None
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik

print(silnia(0))
print(silnia(5))
print(silnia(10))
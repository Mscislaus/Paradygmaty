import math

def rownanie_kwadratowe():
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))

    if a == 0:
        print("To nie jest równanie kwadratowe.")
        return

    delta = b**2 - 4*a*c
    print("Delta:", delta)

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print(f"Dwa pierwiastki: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Jeden pierwiastek: x = {x}")
    else:
        print("Brak pierwiastków rzeczywistych.")
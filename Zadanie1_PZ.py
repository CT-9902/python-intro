# zadanie_1 Programowanie zaawansowane

import math

def calc():
    # Funkcja łączy dwie listy używając zip() i oblicza pierwiastek kwadratowy z sumy par liczb.
    liczby1 = [1, 4, 9, 16]
    liczby2 = [1, 1, 1, 4]
    wyniki = []

    # Łączenie list za pomocą zip() i obliczanie pierwiastka
    for x, y in zip(liczby1, liczby2):
        try:
            suma = x + y
            # math.sqrt() - oblicza pierwiastek kwadratowy
            pierwiastek = math.sqrt(suma)
            wyniki.append(pierwiastek)
        except ValueError:
            # Obsługa błędu gdy suma jest ujemna
            print("Błąd: Suma jest ujemna")
            continue

    return wyniki

# Wywołanie funkcji i wyświetlenie wyników
rezultat = calc()

print("Pierwiastki z sum par liczb:")

for i, wynik in enumerate(rezultat, 1):
    print(f"Para {i}: {wynik}")

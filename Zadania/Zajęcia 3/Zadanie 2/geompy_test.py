from geompy import Kwadrat, Prostokat, Kolo, Szescian, Prostopadloscian, Kula

# Testy figur 2D
print("Kwadrat o boku 4:")
kwadrat = Kwadrat(4)
print(f"Pole: {kwadrat.pole()}")  # Powinno być: 16
print(f"Obwód: {kwadrat.obwod()}")  # Powinno być: 16

print("\nProstokąt o bokach 3 i 5:")
prostokat = Prostokat(3, 5)
print(f"Pole: {prostokat.pole()}")  # Powinno być: 15
print(f"Obwód: {prostokat.obwod()}")  # Powinno być: 16

print("\nKoło o promieniu 2:")
kolo = Kolo(2)
print(f"Pole: {kolo.pole()}")  # Powinno być: ok. 12.566
print(f"Obwód: {kolo.obwod()}")  # Powinno być: ok. 12.566

# Testy figur 3D
print("\nSześcian o boku 3:")
szescian = Szescian(3)
print(f"Objętość: {szescian.objetosc()}")  # Powinno być: 27
print(f"Pole powierzchni: {szescian.pole_powierzchni()}")  # Powinno być: 54

print("\nProstopadłościan o bokach 2, 3, 4:")
prostopadloscian = Prostopadloscian(2, 3, 4)
print(f"Objętość: {prostopadloscian.objetosc()}")  # Powinno być: 24
print(f"Pole powierzchni: {prostopadloscian.pole_powierzchni()}")  # Powinno być: 52

print("\nKula o promieniu 2:")
kula = Kula(2)
print(f"Objętość: {kula.objetosc()}")  # Powinno być: ok. 33.510
print(f"Pole powierzchni: {kula.pole_powierzchni()}")  # Powinno być: ok. 50.265
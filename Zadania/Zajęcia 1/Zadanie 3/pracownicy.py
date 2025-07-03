class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}."


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imie, nazwisko, wiek)  # Wywołujemy __init__ z Osoba
        self.stanowisko = stanowisko
        self.pensja = pensja

    def info_o_pracy(self):
        return f"Pracuję jako {self.stanowisko}, zarabiam {self.pensja} zł."


class Manager(Pracownik):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imie, nazwisko, wiek, stanowisko, pensja)  # Wywołujemy __init__ z Pracownik
        self.zespol = []  # Pusta lista na pracowników

    def przedstaw_sie(self):
        liczba_podwladnych = len(self.zespol)
        return f"{super().przedstaw_sie()} Mam {liczba_podwladnych} Pracowników."

    def dodaj_do_zespolu(self, pracownik):
        self.zespol.append(pracownik)


# Test:
if __name__ == "__main__":
    # Tworzymy managera
    manager = Manager("Anna", "Nowak", 35, "Kierownik", 10000.0)

    # Tworzymy kilku pracowników
    pracownik1 = Pracownik("Jan", "Kowalski", 30, "Programista", 5000.0)
    pracownik2 = Pracownik("Maria", "Wiśniewska", 28, "Analityk", 4500.0)
    pracownik3 = Pracownik("Piotr", "Zieliński", 32, "Tester", 4000.0)

    # Dodajemy pracowników do zespołu managera
    manager.dodaj_do_zespolu(pracownik1)
    manager.dodaj_do_zespolu(pracownik2)
    manager.dodaj_do_zespolu(pracownik3)

    # Wyświetlamy informacje
    print(manager.przedstaw_sie())
    print(manager.info_o_pracy())

    print("\nPracownicy w zespole:")
    for pracownik in manager.zespol:
        print(f"- {pracownik.przedstaw_sie()} {pracownik.info_o_pracy()}")
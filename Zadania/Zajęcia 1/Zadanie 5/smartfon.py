class Telefon:
    def __init__(self, model, producent):
        self.model = model
        self.producent = producent

    def opis(self):
        return f"Telefon: {self.producent} {self.model}"


class Komunikacja:
    def wyslij_wiadomosc(self, odbiorca, tresc):
        return f"Wysłano wiadomość do {odbiorca}: {tresc}"


class Rozrywka:
    def odtworz_muzyke(self, utwor):
        return f"Odtwarzam utwór: {utwor}"


class Smartphone:
    def __init__(self, model, producent):
        self.telefon = Telefon(model, producent)
        self.komunikacja = Komunikacja()
        self.rozrywka = Rozrywka()

    def opis(self):
        return self.telefon.opis()

    def wyslij_wiadomosc(self, odbiorca, tresc):
        return self.komunikacja.wyslij_wiadomosc(odbiorca, tresc)

    def odtworz_muzyke(self, utwor):
        return self.rozrywka.odtworz_muzyke(utwor)


# Test:
if __name__ == "__main__":
    # Tworzymy smartfon
    smartfon = Smartphone("Galaxy S23", "Samsung")

    # Wyświetlamy opis
    print(smartfon.opis())

    # Testujemy funkcje
    print(smartfon.wyslij_wiadomosc("Kasia", "Cześć, co słychać?"))
    print(smartfon.odtworz_muzyke("Imagine - John Lennon"))
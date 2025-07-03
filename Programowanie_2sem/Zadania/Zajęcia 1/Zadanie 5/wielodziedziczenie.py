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

class Smartphone(Telefon, Komunikacja, Rozrywka):
    def __init__(self, model, producent):
        super().__init__(model, producent)

# Test:
if __name__ == "__main__":
    smartfon = Smartphone("Galaxy S23", "Samsung")
    print(smartfon.opis())
    print(smartfon.wyslij_wiadomosc("Kasia", "Cześć, co słychać?"))
    print(smartfon.odtworz_muzyke("Imagine - John Lennon"))
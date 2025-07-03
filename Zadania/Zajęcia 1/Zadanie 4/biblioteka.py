class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def opis(self):
        return f"Tytuł: {self.tytul}, Autor: {self.autor}, Rok wydania: {self.rok_wydania}"

class Ebook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, rozmiar_pliku):
        super().__init__(tytul, autor, rok_wydania)  # Wywołujemy __init__ z Ksiazka
        self.rozmiar_pliku = rozmiar_pliku

    def opis(self):
        return f"{super().opis()}, Rozmiar pliku: {self.rozmiar_pliku} MB"

class Audiobook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, czas_trwania):
        super().__init__(tytul, autor, rok_wydania)  # Wywołujemy __init__ z Ksiazka
        self.czas_trwania = czas_trwania

    def opis(self):
        return f"{super().opis()}, Czas trwania: {self.czas_trwania} minut"

# Test:
if __name__ == "__main__":
    # Tworzymy kilka ebooków
    ebook1 = Ebook("Pan Tadeusz", "Adam Mickiewicz", 1834, 2.5)
    ebook2 = Ebook("Wiedźmin", "Andrzej Sapkowski", 1993, 1.8)

    # Tworzymy kilka audiobooków
    audiobook1 = Audiobook("Lalka", "Bolesław Prus", 1890, 1200)
    audiobook2 = Audiobook("Harry Potter", "J.K. Rowling", 1997, 600)

    # Wyświetlamy opisy
    print("Ebooki:")
    print(ebook1.opis())
    print(ebook2.opis())
    print("\nAudiobooki:")
    print(audiobook1.opis())
    print(audiobook2.opis())
import json

class ModelAI:
    liczba_modeli = 0

    def __init__(self, nazwa_modelu, wersja):
        # Przypisanie nazwę i wersji do konkretnego modelu
        self.nazwa_modelu = nazwa_modelu
        self.wersja = wersja
        # Zwiększanie licznika modeli
        self.nowy_model()

    @classmethod
    def nowy_model(cls):
        # Zwiększa licznik modeli o 1
        cls.liczba_modeli += 1

    @classmethod
    def ile_modeli(cls):
        # Zwraca, ile modeli już stworzono
        return cls.liczba_modeli

    @classmethod
    def z_pliku(cls, nazwa_pliku):
        # Otwieramy plik JSON i wczytujemy dane
        with open(nazwa_pliku, 'r') as plik:
            dane = json.load(plik)
        # Tworzymy nowy model na podstawie danych z JSON
        return cls(dane['name'], dane['version'])

# Przykład użycia:
if __name__ == "__main__":
    # Tworzymy model ręcznie
    model1 = ModelAI("super_model", 1.0)
    print(f"Nazwa modelu: {model1.nazwa_modelu}, Wersja: {model1.wersja}")
    print(f"Ile modeli: {ModelAI.ile_modeli()}")

    # Tworzymy model z pliku JSON
    model2 = ModelAI.z_pliku("model.json")
    print(f"Nazwa modelu z pliku: {model2.nazwa_modelu}, Wersja: {model2.wersja}")
    print(f"Ile modeli: {ModelAI.ile_modeli()}")
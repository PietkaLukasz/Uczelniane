from typing import Dict, Optional

class Biblioteka:
    def __init__(self, ksiazka: Dict[str, str]) -> None:
        self.ksiazka = ksiazka  # Słownik {ISBN: tytuł}

    def znajdz_ksiazke(self, isbn: str) -> Optional[str]:
        return self.ksiazka.get(isbn)  # Zwraca tytuł lub None, jeśli ISBN nie ma
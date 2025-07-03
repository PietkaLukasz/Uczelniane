from typing import Dict, Optional


class Biblioteka:

    def __init__(self, ksiazki: Dict[str, str]) -> None:
        self.ksiazki = ksiazki

    def znajdz_ksiazke(self, isbn: str) -> Optional[str]:
        return self.ksiazki.get(isbn)

    def dodaj_ksiazke(self, isbn: str, tytul: str) -> None:
        self.ksiazki[isbn] = tytul

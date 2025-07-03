from datetime import datetime


class KlasaZakup:
    """Klasa przechowująca informacje o transakcji kupna lub sprzedaży aktywa."""

    def __init__(self, symbol_aktywa: str, typ_aktywa: str, ilosc_aktywa: float, cena_aktywa: float,
                 typ_zakupu: str, data_zakupu: datetime):
        self.symbol_aktywa = symbol_aktywa  # Symbol, np. AAPL
        self.typ_aktywa = typ_aktywa  # Typ, np. Akcje, Obligacje, Surowce
        self.ilosc_aktywa = ilosc_aktywa  # Ile sztuk kupiono lub sprzedano
        self.cena_aktywa = cena_aktywa  # Cena za jedną sztukę
        self.typ_zakupu = typ_zakupu  # "Kupno" lub "Sprzedaż"
        self.data_zakupu = data_zakupu  # Data transakcji
class KlasaAktywo:
    """Klasa przechowująca informacje o aktywie, czyli czymś, co mamy w portfelu, na przykład akcje, obligacje lub surowce."""

    def __init__(self, symbol_aktywa: str, typ_aktywa: str, aktualna_cena_aktywa: float = 0.0):
        self.symbol_aktywa = symbol_aktywa  # Symbol, np. AAPL dla akcji Apple
        self.typ_aktywa = typ_aktywa  # Typ, np. Akcje, Obligacje, Surowce
        self.aktualna_cena_aktywa = aktualna_cena_aktywa  # Aktualna cena za jedną sztukę
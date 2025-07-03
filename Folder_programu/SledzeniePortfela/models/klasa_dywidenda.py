from datetime import datetime


class KlasaDywidenda:
    """Klasa przechowująca informacje o dywidendzie z aktywa."""

    def __init__(self, symbol_aktywa: str, kwota_dywidendy: float, data_dywidendy: datetime):
        self.symbol_aktywa = symbol_aktywa  # Symbol, np. AAPL
        self.kwota_dywidendy = kwota_dywidendy  # Kwota dywidendy
        self.data_dywidendy = data_dywidendy  # Data wypłaty dywidendy
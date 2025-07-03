import pytest
from models.klasa_zakup import KlasaZakup
from models.klasa_portfel import KlasaPortfel
from unittest.mock import Mock
from datetime import datetime


# Mock dla bazy danych
@pytest.fixture
def mock_zarzadca_bazy():
    zarzadca = Mock()
    zarzadca.pobierz_zakupy.return_value = [
        KlasaZakup("TSLA", "Akcje", 10, 281.21, "Kupno", datetime(2023, 1, 1)),  # Kupno 10 TSLA
        KlasaZakup("TSLA", "Akcje", 3, 290.00, "Sprzedaż", datetime(2023, 6, 1))  # Sprzedaż 3 TSLA
    ]
    return zarzadca


def test_pobierz_saldo_na_dzien(mock_zarzadca_bazy):
    portfel = KlasaPortfel(mock_zarzadca_bazy)
    saldo = portfel.pobierz_saldo_na_dzien(datetime(2023, 12, 31))
    assert saldo == {"TSLA": 7}  # 10 - 3 = 7 (zabezpieczenie max(0) nie zadziała, bo saldo dodatnie)


def test_oblicz_wartosc_portfela(mock_zarzadca_bazy):
    portfel = KlasaPortfel(mock_zarzadca_bazy)
    mock_api = Mock()

    # Zmockuj dane S&P 500 z kluczami jako datetime
    data_test = datetime(2023, 12, 31)
    mock_api.pobierz_dane_sp500.return_value = {
        data_test: 4500.0  # Przykładowa cena S&P 500
    }

    # Zmockuj dane historyczne dla TSLA
    mock_api.pobierz_dane_historyczne_aktywa.side_effect = lambda symbol, start, end: {
        datetime(2023, 12, 31): 300.0 if symbol == "TSLA" else 0.0
    }

    dane = portfel.oblicz_wartosc_portfela(mock_api, datetime(2023, 1, 1), datetime(2023, 12, 31))
    assert len(dane) == 1  # Jedna data z mocka
    assert dane[0][1] == 2100.0  # 7 * 300 (saldo po sprzedaży)
import yfinance as yf
from datetime import datetime

class UslugaAPI:
    def pobierz_dane_sp500(self, data_poczatkowa, data_koncowa):
        """Pobiera dane S&P 500 z Yahoo Finance."""
        sp500 = yf.Ticker("^GSPC")
        # Konwersja dat na stringi bez zmiany strefy
        data_poczatkowa_str = data_poczatkowa.strftime('%Y-%m-%d')
        data_koncowa_str = min(data_koncowa, datetime.now()).strftime('%Y-%m-%d')
        dane = sp500.history(start=data_poczatkowa_str, end=data_koncowa_str)
        if dane.empty:
            print(f"Brak danych S&P 500 dla zakresu {data_poczatkowa_str} do {data_koncowa_str}")
        return dane["Close"].to_dict() if not dane.empty else {}

    def pobierz_cene_aktywa(self, symbol):
        """Pobiera aktualną lub ostatnią dostępną cenę aktywa z Yahoo Finance."""
        try:
            akcja = yf.Ticker(symbol)
            dane = akcja.history(period="5d")
            if not dane.empty:
                cena = dane["Close"].dropna().iloc[-1]
                return cena if cena > 0 else None
            print(f"Brak danych ceny dla {symbol}")
            return None
        except Exception as e:
            print(f"Błąd przy pobieraniu ceny dla {symbol}: {e}")
            return None

    def pobierz_dane_historyczne_aktywa(self, symbol, data_poczatkowa, data_koncowa):
        """Pobiera historyczne dane ceny aktywa z Yahoo Finance."""
        try:
            akcja = yf.Ticker(symbol)
            data_poczatkowa_str = data_poczatkowa.strftime('%Y-%m-%d')
            data_koncowa_str = min(data_koncowa, datetime.now()).strftime('%Y-%m-%d')
            dane = akcja.history(start=data_poczatkowa_str, end=data_koncowa_str)
            if dane.empty or len(dane) < 2:
                print(f"Brak pełnych danych dla {symbol} w zakresie {data_poczatkowa_str} do {data_koncowa_str}")
            return dane["Close"].to_dict() if not dane.empty else {}
        except Exception as e:
            print(f"Błąd przy pobieraniu danych historycznych dla {symbol}: {e}")
            return {}
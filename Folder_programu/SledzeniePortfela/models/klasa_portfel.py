from models.klasa_zakup import KlasaZakup
from models.klasa_dywidenda import KlasaDywidenda
from database.zarzadca_bazy_danych import ZarzadcaBazyDanych
from datetime import datetime

class KlasaPortfel:
    """Klasa zarządzająca całym portfelem inwestycyjnym."""

    def __init__(self, zarzadca_bazy_danych: ZarzadcaBazyDanych):
        self.baza_danych = zarzadca_bazy_danych

    def dodaj_zakup(self, zakup: KlasaZakup) -> None:
        """Dodaje nową transakcję (kupno lub sprzedaż) do portfela."""
        self.baza_danych.dodaj_zakup(zakup)

    def dodaj_dywidende(self, dywidenda: KlasaDywidenda) -> None:
        """Dodaje nową dywidendę do portfela."""
        self.baza_danych.dodaj_dywidende(dywidenda)

    def pobierz_zakupy(self, typ_aktywa: str = "Wszystkie") -> list:
        """Pobiera listę wszystkich transakcji z bazy danych, można filtrować po typie aktywa."""
        return self.baza_danych.pobierz_zakupy(typ_aktywa)

    def pobierz_saldo_na_dzien(self, data: datetime) -> dict:
        """Pobiera saldo aktywów na konkretny dzień na podstawie transakcji."""
        zakupy = self.pobierz_zakupy()
        saldo = {}
        for zakup in zakupy:
            if zakup.data_zakupu <= data:
                if zakup.symbol_aktywa not in saldo:
                    saldo[zakup.symbol_aktywa] = 0
                if zakup.typ_zakupu == "Kupno":
                    saldo[zakup.symbol_aktywa] += zakup.ilosc_aktywa
                elif zakup.typ_zakupu == "Sprzedaż":
                    saldo[zakup.symbol_aktywa] -= zakup.ilosc_aktywa
                saldo[zakup.symbol_aktywa] = max(saldo[zakup.symbol_aktywa], 0)
        return saldo

    def oblicz_wartosc_portfela(self, usluga_api, data_poczatkowa: datetime, data_koncowa: datetime) -> list:
        """Oblicza historyczną wartość portfela na podstawie cen i sald na każdy dzień."""
        dane_historyczne = []
        dane_sp500 = usluga_api.pobierz_dane_sp500(data_poczatkowa, data_koncowa)
        for data, cena_sp in dane_sp500.items():
            saldo = self.pobierz_saldo_na_dzien(data)
            wartosc = sum(saldo[s] * usluga_api.pobierz_dane_historyczne_aktywa(s, data, data).get(data, 0)
                          for s in saldo.keys() if s in saldo and saldo[s] > 0)
            dane_historyczne.append((data, wartosc))
        return dane_historyczne

    def pobierz_alokacje_aktyw(self) -> dict:
        """Zwraca, jak dużo mamy każdego typu aktywa (np. Akcje, Obligacje, Surowce)."""
        zakupy = self.pobierz_zakupy()
        alokacja = {}
        for zakup in zakupy:
            if zakup.typ_aktywa not in alokacja:
                alokacja[zakup.typ_aktywa] = 0
            if zakup.typ_zakupu == "Kupno":
                alokacja[zakup.typ_aktywa] += zakup.ilosc_aktywa * zakup.cena_aktywa
            else:
                alokacja[zakup.typ_aktywa] -= zakup.ilosc_aktywa * zakup.cena_aktywa
        return alokacja
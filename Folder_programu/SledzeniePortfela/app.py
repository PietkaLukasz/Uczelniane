import streamlit as streamlit
import pandas as pd
import matplotlib.pyplot as pyplot
from datetime import datetime, date, timezone
from models.klasa_aktywo import KlasaAktywo
from models.klasa_zakup import KlasaZakup
from models.klasa_dywidenda import KlasaDywidenda
from models.klasa_portfel import KlasaPortfel
from database.zarzadca_bazy_danych import ZarzadcaBazyDanych
from services.usluga_api import UslugaAPI

try:
    streamlit.title("Śledzenie Portfela Inwestycyjnego")

    # Inicjalizacja z automatyczną synchronizacją bazy
    zarzadca_bazy_danych = ZarzadcaBazyDanych()
    portfel = KlasaPortfel(zarzadca_bazy_danych)
    usluga_api = UslugaAPI()

    # Restart portfela
    if streamlit.button("Restartuj portfel"):
        zarzadca_bazy_danych.wyczysc_baze()
        zakupy = portfel.pobierz_zakupy()
    else:
        zakupy = portfel.pobierz_zakupy()

    # Formularz zakupu
    with streamlit.form("formularz_dodaj_zakup"):
        streamlit.header("Dodaj nowy zakup lub sprzedaż")
        typ_aktywa = streamlit.selectbox("Wybierz typ aktywa", ["Akcje", "Obligacje", "Surowce"])
        symbol_aktywa = streamlit.text_input("Podaj symbol aktywa (np. AAPL)").upper()
        ilosc_aktywa = streamlit.number_input("Podaj ilość", min_value=0.0, step=0.01)
        cena_aktywa = streamlit.number_input("Podaj cenę za jedną sztukę", min_value=0.0, step=0.01)
        typ_zakupu = streamlit.radio("Wybierz typ transakcji", ["Kupno", "Sprzedaż"])
        data_zakupu = streamlit.date_input("Podaj datę zakupu", value=date.today())
        przycisk_dodaj = streamlit.form_submit_button("Dodaj transakcję")
        if przycisk_dodaj and symbol_aktywa and ilosc_aktywa > 0 and cena_aktywa > 0:
            zakup = KlasaZakup(symbol_aktywa, typ_aktywa, ilosc_aktywa, cena_aktywa, typ_zakupu, data_zakupu)
            portfel.dodaj_zakup(zakup)
            zakupy = portfel.pobierz_zakupy()  # Odśwież listę po dodaniu
            streamlit.success(f"Dodano transakcję: {typ_zakupu} {ilosc_aktywa} {symbol_aktywa}")

    # Formularz dywidendy
    with streamlit.form("formularz_dodaj_dywidende"):
        streamlit.header("Dodaj nową dywidendę")
        symbol_dywidendy = streamlit.text_input("Podaj symbol aktywa dla dywidendy").upper()
        kwota_dywidendy = streamlit.number_input("Podaj kwotę dywidendy", min_value=0.0, step=0.01)
        data_dywidendy = streamlit.date_input("Podaj datę dywidendy", value=date.today())
        przycisk_dywidenda = streamlit.form_submit_button("Dodaj dywidendę")
        if przycisk_dywidenda and symbol_dywidendy and kwota_dywidendy > 0:
            dywidenda = KlasaDywidenda(symbol_dywidendy, kwota_dywidendy, data_dywidendy)
            portfel.dodaj_dywidende(dywidenda)
            streamlit.success(f"Dodano dywidendę: {kwota_dywidendy} dla {symbol_dywidendy}")

    # Tabela transakcji
    streamlit.header("Lista Twoich transakcji")
    if zakupy:
        dane_tabela = pd.DataFrame(
            [(z.symbol_aktywa, z.typ_aktywa, z.ilosc_aktywa, z.cena_aktywa, z.typ_zakupu, z.data_zakupu)
             for z in zakupy],
            columns=["Symbol", "Typ aktywa", "Ilość", "Cena zakupu", "Typ transakcji", "Data"]
        )
        aktualne_ceny = {z.symbol_aktywa: usluga_api.pobierz_cene_aktywa(z.symbol_aktywa) for z in zakupy}
        for index, row in dane_tabela.iterrows():
            symbol = row["Symbol"]
            cena_zakupu = row["Cena zakupu"]
            cena_aktualna = aktualne_ceny.get(symbol, cena_zakupu)
            wartosc_zakupu = row["Ilość"] * cena_zakupu
            wartosc_aktualna = row["Ilość"] * cena_aktualna
            zysk_strata = wartosc_aktualna - wartosc_zakupu
            dane_tabela.at[index, "Wartość zakupu"] = f"{wartosc_zakupu:.2f} USD"
            dane_tabela.at[index, "Wartość aktualna"] = f"{wartosc_aktualna:.2f} USD"
            dane_tabela.at[index, "Zysk/Strata"] = f"{zysk_strata:.2f} USD"
        streamlit.dataframe(dane_tabela)
    else:
        streamlit.info("Brak transakcji w portfelu.")

    # Filtrowanie
    streamlit.header("Filtruj transakcje po typie aktywa")
    wybrany_typ_aktywa = streamlit.selectbox("Wybierz typ aktywa do filtrowania", ["Wszystkie", "Akcje", "Obligacje", "Surowce"])
    if wybrany_typ_aktywa != "Wszystkie":
        zakupy_filtr = [z for z in zakupy if z.typ_aktywa == wybrany_typ_aktywa]
        if zakupy_filtr:
            dane_tabela_filtr = pd.DataFrame(
                [(z.symbol_aktywa, z.typ_aktywa, z.ilosc_aktywa, z.cena_aktywa, z.typ_zakupu, z.data_zakupu)
                 for z in zakupy_filtr],
                columns=["Symbol", "Typ aktywa", "Ilość", "Cena zakupu", "Typ transakcji", "Data"]
            )
            streamlit.dataframe(dane_tabela_filtr)
        else:
            streamlit.info("Brak transakcji dla wybranego typu aktywa.")

    # Porównanie z S&P 500 z wyborem dat
    streamlit.header("Porównanie portfela z S&P 500")
    if zakupy:
        # Konwersja dat z st.date_input na datetime
        data_poczatkowa = datetime.combine(streamlit.date_input("Data początkowa porównania", value=date(2000, 1, 1)), datetime.min.time())
        data_koncowa = datetime.combine(streamlit.date_input("Data końcowa porównania", value=date.today()), datetime.min.time())
        dane_sp = usluga_api.pobierz_dane_sp500(data_poczatkowa, data_koncowa)
        dane_port = portfel.oblicz_wartosc_portfela(usluga_api, data_poczatkowa, data_koncowa)

        # Wyświetlanie wykresu
        if dane_sp and dane_port:
            fig, ax = pyplot.subplots()
            daty_sp = [d for d, _ in sorted(dane_sp.items())]
            wartosci_sp = [dane_sp[d] for d in daty_sp]
            daty_port = [d for d, _ in sorted(dane_port)]
            wartosci_port = [v for _, v in sorted(dane_port)]
            ax.plot(daty_sp, wartosci_sp, label="S&P 500")
            ax.plot(daty_port, wartosci_port, label="Twój portfel")
            ax.legend()
            streamlit.pyplot(fig)
        else:
            streamlit.warning("Nie udało się pobrać danych do porównania. Sprawdź daty (do 30 czerwca 2025) lub dostępność API. Ustaw zakres od 2000-01-01.")

        # Wartość portfela
        if dane_port:
            wartosc_calkowita = dane_port[-1][1] if dane_port else 0
        else:
            wartosc_calkowita = sum(z.ilosc_aktywa * usluga_api.pobierz_cene_aktywa(z.symbol_aktywa) for z in zakupy if z.typ_zakupu == "Kupno") - sum(z.ilosc_aktywa * usluga_api.pobierz_cene_aktywa(z.symbol_aktywa) for z in zakupy if z.typ_zakupu == "Sprzedaż")
        streamlit.write(f"Całkowita wartość portfela: {wartosc_calkowita:.2f} USD")

    # Alokacja aktywów
    streamlit.header("Alokacja aktywów w portfelu")
    alokacja = portfel.pobierz_alokacje_aktyw()
    if alokacja:
        streamlit.bar_chart(alokacja)
    else:
        streamlit.info("Brak alokacji do wyświetlenia.")

except Exception as e:
    streamlit.error(f"Wystąpił błąd: {e}")
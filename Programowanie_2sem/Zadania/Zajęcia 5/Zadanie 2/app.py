import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from datetime import date


def polacz_z_baza(sciezka: str = "sales.db") -> sqlite3.Connection:
    return sqlite3.connect(sciezka)


def pobierz_dane(polaczenie: sqlite3.Connection, produkt: str = None) -> pd.DataFrame:
    """Pobiera dane z tabeli sales z opcjonalnym filtrem po produkcie."""
    zapytanie = "SELECT id, product, date, price, quantity FROM sales"
    if produkt:
        zapytanie += " WHERE product = ?"
        df = pd.read_sql_query(zapytanie, polaczenie, params=(produkt,))
    else:
        df = pd.read_sql_query(zapytanie, polaczenie)
    return df


def dodaj_rekord(polaczenie: sqlite3.Connection, produkt: str, ilosc: int, cena: float, data: str) -> None:
    """Dodaje nowy rekord sprzedaży do bazy."""
    kursor = polaczenie.cursor()
    kursor.execute(
        "INSERT INTO sales (product, date, price, quantity) VALUES (?, ?, ?, ?)",
        (produkt, data, cena, ilosc)
    )
    polaczenie.commit()


def main():
    """Główna funkcja aplikacji Streamlit."""
    st.title("Aplikacja sprzedaży")

    # Połączenie z bazą
    try:
        polaczenie = polacz_z_baza("sales.db")
    except sqlite3.Error as e:
        st.error(f"Błąd bazy danych: {e}")
        return

    # Formularz dodawania rekordu
    st.header("Dodaj nowe zadanie")
    with st.form(key="dodaj_form"):
        produkt = st.text_input("Produkt", placeholder="Wpisz nazwę produktu")
        ilosc = st.number_input("Ilość", min_value=1, step=1)
        cena = st.number_input("Cena jednostkowa (zł)", min_value=0.01, step=0.01)
        data = st.date_input("Data sprzedaży", value=date.today())
        zatwierdz = st.form_submit_button("Dodaj")

        if zatwierdz and produkt:
            dodaj_rekord(polaczenie, produkt, ilosc, cena, str(data))
            st.success("Dodano nowy rekord sprzedaży!")
            st.balloons()

    # Filtrowanie danych
    st.header("Dane sprzedaży")
    pokaz_wszystkie = st.checkbox("Pokaż wszystkie produkty", value=True)
    df = pobierz_dane(polaczenie)
    produkty = ["Wszystkie"] + sorted(df["product"].unique().tolist())
    wybrany_produkt = st.selectbox("Filtruj po produkcie", produkty)

    if not pokaz_wszystkie and wybrany_produkt != "Wszystkie":
        df = pobierz_dane(polaczenie, wybrany_produkt)

    st.dataframe(df)

    # Wykres 1: Sprzedaż dzienna (ilość × cena)
    st.header("Sprzedaż dzienna")
    df["wartosc"] = df["price"] * df["quantity"]
    dzienna_sprzedaz = df.groupby("date")["wartosc"].sum().reset_index()
    fig1 = px.line(dzienna_sprzedaz, x="date", y="wartosc", title="Sprzedaż dzienna (wartość w zł)")
    st.plotly_chart(fig1)

    # Wykres 2: Suma sprzedanych produktów według typu
    st.header("Suma sprzedanych produktów według typu")
    suma_produktow = df.groupby("product")["quantity"].sum().reset_index()
    fig2 = px.bar(suma_produktow, x="product", y="quantity", title="Suma sprzedanych sztuk")
    st.plotly_chart(fig2)

    # Zamykamy połączenie
    polaczenie.close()


if __name__ == "__main__":
    main()
import sqlite3
from typing import List, Tuple

def polacz_z_baza(sciezka: str = "sales.db") -> sqlite3.Connection:
    """Łączy się z bazą danych SQLite."""
    return sqlite3.connect(sciezka)

def wyswietl_sprzedaz_laptopow(polaczenie: sqlite3.Connection) -> None:
    """a) Wyświetla sprzedaż tylko produktu 'Laptop'."""
    print("\nSprzedaż produktu 'Laptop':")
    kursor = polaczenie.cursor()
    kursor.execute("SELECT * FROM sales WHERE product = 'Laptop'")
    wyniki = kursor.fetchall()
    for wiersz in wyniki:
        print(wiersz)

def wyswietl_sprzedaz_z_dni(polaczenie: sqlite3.Connection, dni: List[str]) -> None:
    """b) Wyświetla dane z dni 2025-05-07 i 2025-05-08."""
    print("\nSprzedaż z dni 2025-05-07 i 2025-05-08:")
    kursor = polaczenie.cursor()
    kursor.execute("SELECT * FROM sales WHERE date IN (?, ?)", dni)
    wyniki = kursor.fetchall()
    for wiersz in wyniki:
        print(wiersz)

def wyswietl_sprzedaz_powyzej_ceny(polaczenie: sqlite3.Connection, cena: float) -> None:
    """c) Wyświetla transakcje z ceną jednostkową powyżej 200 zł."""
    print("\nTransakcje z ceną jednostkową powyżej 200 zł:")
    kursor = polaczenie.cursor()
    kursor.execute("SELECT * FROM sales WHERE price > ?", (cena,))
    wyniki = kursor.fetchall()
    for wiersz in wyniki:
        print(wiersz)

def oblicz_wartosc_sprzedazy(polaczenie: sqlite3.Connection) -> None:
    """d) Oblicza łączną wartość sprzedaży dla każdego produktu."""
    print("\nŁączna wartość sprzedaży dla każdego produktu:")
    kursor = polaczenie.cursor()
    kursor.execute("SELECT product, SUM(price * quantity) AS wartosc FROM sales GROUP BY product")
    wyniki = kursor.fetchall()
    for produkt, wartosc in wyniki:
        print(f"Produkt: {produkt}, Wartość: {wartosc} zł")

def znajdz_dzien_najwiekszej_sprzedazy(polaczenie: sqlite3.Connection) -> None:
    """e) Znajduje dzień z największą liczbą sprzedanych sztuk."""
    print("\nDzień z największą liczbą sprzedanych sztuk:")
    kursor = polaczenie.cursor()
    kursor.execute("SELECT date, SUM(quantity) AS ilosc_sztuk FROM sales GROUP BY date ORDER BY ilosc_sztuk DESC LIMIT 1")
    wynik = kursor.fetchone()
    if wynik:
        print(f"Dzień: {wynik[0]}, Sprzedane sztuki: {wynik[1]}")

def main():
    """Główna funkcja wykonująca wszystkie zapytania."""
    try:
        polaczenie = polacz_z_baza("sales.db")
        wyswietl_sprzedaz_laptopow(polaczenie)
        wyswietl_sprzedaz_z_dni(polaczenie, ["2025-05-07", "2025-05-08"])
        wyswietl_sprzedaz_powyzej_ceny(polaczenie, 200.0)
        oblicz_wartosc_sprzedazy(polaczenie)
        znajdz_dzien_najwiekszej_sprzedazy(polaczenie)
        polaczenie.close()
    except sqlite3.Error as e:
        print(f"Błąd bazy danych: {e}")

if __name__ == "__main__":
    main()
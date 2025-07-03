import sqlite3


def sprawdz_strukture_bazy(sciezka: str = "sales.db") -> None:
    """Sprawdza strukturę bazy danych."""
    try:
        polaczenie = sqlite3.connect(sciezka)
        kursor = polaczenie.cursor()

        # Pokazujemy nazwy tabel
        kursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tabele = kursor.fetchall()
        print("Tabele w bazie:", tabele)

        # Pokazujemy kolumny tabeli 'sales'
        kursor.execute("PRAGMA table_info(sales);")
        kolumny = kursor.fetchall()
        print("Kolumny tabeli 'sales':", kolumny)

        polaczenie.close()
    except sqlite3.Error as e:
        print(f"Błąd bazy danych: {e}")


if __name__ == "__main__":
    sprawdz_strukture_bazy()
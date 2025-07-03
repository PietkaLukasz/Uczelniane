import sqlite3
from datetime import datetime, timezone
from models.klasa_zakup import KlasaZakup
from models.klasa_dywidenda import KlasaDywidenda
import os
import paramiko
import streamlit

DATABASE_PATH = r"E:\Py-Projects\Roboczy\Programowanie_II_Poziomu\Na_Zaliczenie\Folder_programu\SledzeniePortfela\data\portfel_baza_danych.db"
SERVER_PATH = "/home/student/SledzeniePortfela/data/portfel_baza_danych.db"
SSH_HOST = "127.0.0.1"
SSH_PORT = 2222
SSH_USERNAME = "student"
SSH_PASSWORD = "student"

class ZarzadcaBazyDanych:
    def __init__(self):
        if not os.path.exists(DATABASE_PATH):
            self._download_database()
        self.nazwa_bazy_danych = DATABASE_PATH
        #self.wyczysc_duplikaty() # zakomentowane czysci duplikaty z bazy danych
        self.utworz_tabele()

    def _get_connection(self):
        return sqlite3.connect(self.nazwa_bazy_danych)

    def _download_database(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(SSH_HOST, port=SSH_PORT, username=SSH_USERNAME, password=SSH_PASSWORD)
            sftp = ssh.open_sftp()
            sftp.get(SERVER_PATH, DATABASE_PATH)
            sftp.close()
            ssh.close()
            streamlit.success("Baza danych pobrana z serwera!")
        except Exception as e:
            streamlit.error(f"Błąd pobierania bazy: {e}")
            with sqlite3.connect(DATABASE_PATH) as conn:
                conn.commit()

    def _upload_database(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(SSH_HOST, port=SSH_PORT, username=SSH_USERNAME, password=SSH_PASSWORD)
            sftp = ssh.open_sftp()
            sftp.put(DATABASE_PATH, SERVER_PATH)
            sftp.close()
            ssh.close()
            streamlit.success("Baza danych wysłana na serwer!")
        except Exception as e:
            streamlit.error(f"Błąd wysyłania bazy: {e}")

    def utworz_tabele(self) -> None:
        try:
            with sqlite3.connect(self.nazwa_bazy_danych) as polaczenie:
                kursor = polaczenie.cursor()
                kursor.execute("""
                    CREATE TABLE IF NOT EXISTS zakupy (
                        identyfikator INTEGER PRIMARY KEY AUTOINCREMENT,
                        symbol_aktywa TEXT NOT NULL,
                        typ_aktywa TEXT NOT NULL,
                        ilosc_aktywa REAL NOT NULL,
                        cena_aktywa REAL NOT NULL,
                        typ_zakupu TEXT NOT NULL,
                        data_zakupu TEXT NOT NULL
                    )
                """)
                kursor.execute("""
                    CREATE TABLE IF NOT EXISTS dywidendy (
                        identyfikator INTEGER PRIMARY KEY AUTOINCREMENT,
                        symbol_aktywa TEXT NOT NULL,
                        kwota_dywidendy REAL NOT NULL,
                        data_dywidendy TEXT NOT NULL
                    )
                """)
                polaczenie.commit()
        except Exception as e:
            streamlit.error(f"Błąd tworzenia tabel: {e}")

    def dodaj_zakup(self, zakup: KlasaZakup) -> None:
        try:
            with sqlite3.connect(self.nazwa_bazy_danych) as polaczenie:
                kursor = polaczenie.cursor()
                kursor.execute("""
                    INSERT INTO zakupy (symbol_aktywa, typ_aktywa, ilosc_aktywa, cena_aktywa, typ_zakupu, data_zakupu)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (zakup.symbol_aktywa, zakup.typ_aktywa, zakup.ilosc_aktywa,
                      zakup.cena_aktywa, zakup.typ_zakupu, zakup.data_zakupu.isoformat()))
                polaczenie.commit()
                self._upload_database()
                streamlit.success("Transakcja dodana pomyślnie!")
        except Exception as e:
            streamlit.error(f"Błąd przy dodawaniu transakcji: {e}")

    def dodaj_dywidende(self, dywidenda: KlasaDywidenda) -> None:
        try:
            with sqlite3.connect(self.nazwa_bazy_danych) as polaczenie:
                kursor = polaczenie.cursor()
                kursor.execute("""
                    INSERT INTO dywidendy (symbol_aktywa, kwota_dywidendy, data_dywidendy)
                    VALUES (?, ?, ?)
                """, (dywidenda.symbol_aktywa, dywidenda.kwota_dywidendy, dywidenda.data_dywidendy.isoformat()))
                polaczenie.commit()
                self._upload_database()
                streamlit.success("Dywidenda dodana pomyślnie!")
        except Exception as e:
            streamlit.error(f"Błąd przy dodawaniu dywidendy: {e}")

    def pobierz_zakupy(self, typ_aktywa: str = "Wszystkie") -> list:
        try:
            with sqlite3.connect(self.nazwa_bazy_danych) as polaczenie:
                kursor = polaczenie.cursor()
                if typ_aktywa == "Wszystkie":
                    kursor.execute(
                        "SELECT symbol_aktywa, typ_aktywa, ilosc_aktywa, cena_aktywa, typ_zakupu, data_zakupu FROM zakupy")
                else:
                    kursor.execute("""
                        SELECT symbol_aktywa, typ_aktywa, ilosc_aktywa, cena_aktywa, typ_zakupu, data_zakupu
                        FROM zakupy WHERE typ_aktywa = ?
                    """, (typ_aktywa,))
                zakupy = [
                    KlasaZakup(t[0], t[1], t[2], t[3], t[4], datetime.fromisoformat(t[5]).replace(tzinfo=timezone.utc))
                    for t in kursor.fetchall()
                ]
                return zakupy
        except Exception as e:
            streamlit.error(f"Błąd przy pobieraniu zakupów: {e}")
            return []

    def wyczysc_baze(self):
        try:
            with sqlite3.connect(self.nazwa_bazy_danych) as polaczenie:
                kursor = polaczenie.cursor()
                kursor.execute("DELETE FROM zakupy")
                kursor.execute("DELETE FROM dywidendy")
                polaczenie.commit()
                self._upload_database()
                streamlit.success("Portfel zresetowany!")
        except Exception as e:
            streamlit.error(f"Błąd przy resetowaniu portfela: {e}")

    def wyczysc_duplikaty(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM zakupy WHERE rowid NOT IN (SELECT MIN(rowid) FROM zakupy GROUP BY symbol_aktywa, data_zakupu, typ_zakupu, ilosc_aktywa);")
        conn.commit()
        conn.close()
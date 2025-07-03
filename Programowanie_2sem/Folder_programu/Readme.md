# Śledzenie Portfela Inwestycyjnego

Aplikacja do śledzenia portfela inwestycyjnego z porównaniem do S&P 500.

# Wymagania
- **Python 3.8+**
- Biblioteki: Zobacz `requirements.txt`
- **Wirtualka z Ubuntu Server**: Wymagana (https://ubuntu.com/download/server) do synchronizacji bazy danych SQLite.
- SQLite (wbudowane w Python, ale upewnij się, że działa).
- Narzędzia SSH (np. `scp` lub biblioteka `paramiko`)

# Uruchomienie lokalnie
1. Zainstaluj wymagane biblioteki(z pliku w folderze programu):
   ```bash
   `pip install -r requirements.txt`
2. Skonfiguruj maszynę wirtualną i połącz się z nią przez ssh w celu łatwiejszego przepisywania poleceń. 
SSH Jest wymagane też do działania programu.
3. Pobierz, lub użytj dostarczonej bazy danych: 
Plik `data/portfel_baza_danych.db` jest dołączony do
repozytorium z minimalnymi danymi startowymi. 

# Synchronizacja z Ubuntu na maszynie wirtualnej za pomocą SSH:
Po odpaleniu maszyny wirtualnej, otwórz nową konsolę cmd/powershell do wykonania kroku 1). Krok nr 2) możesz zastosowac w plikach zmieniając kod. 
1) Użyj scp:
2) `p -P 2222 student@localhost:/home/student/SledzeniePortfela/data/portfel_baza_danych.db data/portfel_baza_danych.db`
2) Lub z użyciem paramiko
3) `import paramiko
		ssh = paramiko.SSHClient()
		ssh.connect('localhost', port=2222, username='student', password='student')
		sftp = ssh.open_sftp()
		sftp.get('/home/student/SledzeniePortfela/data/portfel_baza_danych.db', 'data/portfel_baza_danych.db')
		sftp.close()
		ssh.close()`
	
4) W pliku programu`database/zarzadca_bazy_danych.py` znajdują się ścieżki do łączenia i zarządzania bazą danych na maszynie wirtualnej. Je trzeba zmienić na swoje lokalne adresy, oraz inne dane. 
	WAŻNE: Dostosuj hasło i ścieżki do swojej konfiguracji
	
6. uruchom aplikacje

`streamlit run app.py --server.port=8501`

Otwórz przeglądarke na: http://localhost:8501


# Uwagi
1. Program został stworzony z myślą, jako projekt zaliczeniowy na uniwersytecie Łódzkim. 
2. W projekcie została zastosowana nieoficjalna biblioteka `yfinance` w wersji 0.2.63 jako element edukacyjny i obrazujący możliwości koncepcji samego projektu. Z tego powodu sam projekt nie może być jakkolwiek komercjalizowany. 
W przypadku rozwijania projektu i jego komercjalizacji, konieczny jest zakup odpowiedniego API i jego synchronizacji z programem.
3. Kod został częściowo opracowany przy wykorzystaniu technik Vibe-codingu z xAI (Grok 3) – dziękuję za pomoc w debugowaniu i optymalizacji!


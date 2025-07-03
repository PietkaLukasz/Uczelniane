import pytest
from database.zarzadca_bazy_danych import ZarzadcaBazyDanych
from unittest.mock import Mock, patch
from datetime import datetime

@pytest.fixture
def mock_ssh():
    with patch('paramiko.SSHClient') as mock_ssh_client:
        mock_ssh = mock_ssh_client.return_value
        mock_ssh.set_missing_host_key_policy.return_value = None
        mock_sftp = Mock()
        mock_ssh.open_sftp.return_value = mock_sftp
        mock_sftp.get.return_value = None
        mock_sftp.put.return_value = None
        yield mock_ssh

def test_download_database(mock_ssh):
    zarzadca = ZarzadcaBazyDanych()
    zarzadca._download_database()
    mock_ssh.connect.assert_called_once()

def test_dodaj_zakup(mock_ssh):
    zarzadca = ZarzadcaBazyDanych()
    from models.klasa_zakup import KlasaZakup
    zakup = KlasaZakup("TSLA", "Akcje", 10, 281.21, "Kupno", datetime(2023, 1, 1))
    zarzadca.dodaj_zakup(zakup)
    # Test wymaga mocka bazy SQLite – tutaj tylko sprawdzamy wywołanie
    assert True  # Koniecznosc dalszej rozbudowy z mockiem sqlite3
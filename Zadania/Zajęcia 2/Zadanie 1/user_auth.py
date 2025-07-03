class UserNotFoundError(Exception):
    pass

class WrongPasswordError(Exception):
    pass

class UserAuth:
    def __init__(self, users):
        self.users = users  # Słownik z użytkownikami i hasłami

    def login(self, username, password):
        # Sprawdzam, czy użytkownik istnieje
        if username not in self.users:
            raise UserNotFoundError(f"Użytkownik {username} nie istnieje!")
        # Sprawdzam, czy hasło jest poprawne
        if self.users[username] != password:
            raise WrongPasswordError(f"Złe hasło dla użytkownika {username}!")
        # Jeśli wszystko OK, komunikat o sukcesie
        return f"Logowanie udane dla użytkownika {username}!"
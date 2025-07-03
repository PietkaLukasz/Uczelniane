from user_auth import UserAuth, UserNotFoundError, WrongPasswordError

if __name__ == "__main__":
    auth = UserAuth({"admin": "1234", "user": "abcd"})

    # Test 1: Poprawne logowanie
    try:
        print(auth.login("admin", "1234"))
    except UserNotFoundError as e:
        print(f"Błąd: {e}")
    except WrongPasswordError as e:
        print(f"Błąd: {e}")
    except Exception as e:
        print(f"Inny błąd: {e}")

    # Test 2: Nieistniejący użytkownik
    try:
        print(auth.login("unknown", "pass"))
    except UserNotFoundError as e:
        print(f"Błąd: {e}")
    except WrongPasswordError as e:
        print(f"Błąd: {e}")
    except Exception as e:
        print(f"Inny błąd: {e}")

    # Test 3: Złe hasło
    try:
        print(auth.login("user", "wrongpass"))
    except UserNotFoundError as e:
        print(f"Błąd: {e}")
    except WrongPasswordError as e:
        print(f"Błąd: {e}")
    except Exception as e:
        print(f"Inny błąd: {e}")
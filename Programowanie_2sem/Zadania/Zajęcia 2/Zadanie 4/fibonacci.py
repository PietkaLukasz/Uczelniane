def fibonacci():
    a, b = 0, 1
    while True:
        yield a  # Zwraca aktualną liczbę
        a, b = b, a + b  # Oblicza kolejną liczbę
class Matrix:
    def __init__(self, a, b, c, d):
        # Elementy macierzy
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        # Dodanie macierze: [a, b; c, d] + [e, f; g, h]
        return Matrix(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c,
            self.d + other.d
        )

    def __mul__(self, other):
        # Mnożenie macierzy według wzoru
        return Matrix(
            self.a * other.a + self.b * other.c,  # a*e + b*g
            self.a * other.b + self.b * other.d,  # a*f + b*h
            self.c * other.a + self.d * other.c,  # c*e + d*g
            self.c * other.b + self.d * other.d  # c*f + d*h
        )

    def __str__(self):
        # Ładne wyświetlanie macierzy, np. [3, 2; 4, 6]
        return f"[{self.a}, {self.b};\n {self.c}, {self.d}]"

    def __repr__(self):
        # Pokazuje, jak stworzyć obiekt, np. Matrix(4, 4, 10, 8)
        return f"Matrix({self.a}, {self.b}, {self.c}, {self.d})"


# Przykład użycia:
if __name__ == "__main__":
    m1 = Matrix(1, 2, 3, 4)
    m2 = Matrix(2, 0, 1, 2)

    # Dodawanie
    m3 = m1 + m2
    print("Wynik dodawania:")
    print(m3)

    # Mnożenie
    m4 = m1 * m2
    print("Wynik mnożenia:")
    print(m4)

    # Reprezentacja
    print("Reprezentacja m4:")
    print(repr(m4))
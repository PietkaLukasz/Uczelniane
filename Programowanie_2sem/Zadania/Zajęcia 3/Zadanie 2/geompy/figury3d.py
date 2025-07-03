from typing import Union
import math


class Szescian:
    """Klasa reprezentująca sześcian."""

    def __init__(self, bok: Union[int, float]) -> None:
        """Inicjalizuje sześcian z podaną długością boku.

        Args:
            bok: Długość boku sześcianu.
        """
        if bok <= 0:
            raise ValueError("Bok musi być większy od zera!")
        self.bok = bok

    def objetosc(self) -> Union[int, float]:
        """Zwraca objętość sześcianu."""
        return self.bok ** 3

    def pole_powierzchni(self) -> Union[int, float]:
        """Zwraca pole powierzchni sześcianu."""
        return 6 * self.bok ** 2


class Prostopadloscian:
    """Klasa reprezentująca prostopadłościan."""

    def __init__(self, bok_a: Union[int, float], bok_b: Union[int, float], bok_c: Union[int, float]) -> None:
        """Inicjalizuje prostopadłościan z podanymi bokami.

        Args:
            bok_a: Długość pierwszego boku.
            bok_b: Długość drugiego boku.
            bok_c: Długość trzeciego boku.
        """
        if bok_a <= 0 or bok_b <= 0 or bok_c <= 0:
            raise ValueError("Boki muszą być większe od zera!")
        self.bok_a = bok_a
        self.bok_b = bok_b
        self.bok_c = bok_c

    def objetosc(self) -> Union[int, float]:
        """Zwraca objętość prostopadłościanu."""
        return self.bok_a * self.bok_b * self.bok_c

    def pole_powierzchni(self) -> Union[int, float]:
        """Zwraca pole powierzchni prostopadłościanu."""
        return 2 * (self.bok_a * self.bok_b + self.bok_a * self.bok_c + self.bok_b * self.bok_c)


class Kula:
    """Klasa reprezentująca kulę."""

    def __init__(self, promien: Union[int, float]) -> None:
        """Inicjalizuje kulę z podanym promieniem.

        Args:
            promien: Promień kuli.
        """
        if promien <= 0:
            raise ValueError("Promień musi być większy od zera!")
        self.promien = promien

    def objetosc(self) -> float:
        """Zwraca objętość kuli."""
        return (4 / 3) * math.pi * self.promien ** 3

    def pole_powierzchni(self) -> float:
        """Zwraca pole powierzchni kuli."""
        return 4 * math.pi * self.promien ** 2
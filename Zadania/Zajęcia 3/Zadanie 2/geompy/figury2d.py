from typing import Union
import math


class Kwadrat:
    """Klasa reprezentująca kwadrat."""

    def __init__(self, bok: Union[int, float]) -> None:
        """Inicjalizuje kwadrat z podaną długością boku.

        Args:
            bok: Długość boku kwadratu.
        """
        if bok <= 0:
            raise ValueError("Bok musi być większy od zera!")
        self.bok = bok

    def pole(self) -> Union[int, float]:
        """Zwraca pole kwadratu."""
        return self.bok ** 2

    def obwod(self) -> Union[int, float]:
        """Zwraca obwód kwadratu."""
        return 4 * self.bok


class Prostokat:
    """Klasa reprezentująca prostokąt."""

    def __init__(self, bok_a: Union[int, float], bok_b: Union[int, float]) -> None:
        """Inicjalizuje prostokąt z podanymi bokami.

        Args:
            bok_a: Długość pierwszego boku.
            bok_b: Długość drugiego boku.
        """
        if bok_a <= 0 or bok_b <= 0:
            raise ValueError("Boki muszą być większe od zera!")
        self.bok_a = bok_a
        self.bok_b = bok_b

    def pole(self) -> Union[int, float]:
        """Zwraca pole prostokąta."""
        return self.bok_a * self.bok_b

    def obwod(self) -> Union[int, float]:
        """Zwraca obwód prostokąta."""
        return 2 * (self.bok_a + self.bok_b)


class Kolo:
    """Klasa reprezentująca koło."""

    def __init__(self, promien: Union[int, float]) -> None:
        """Inicjalizuje koło z podanym promieniem.

        Args:
            promien: Promień koła.
        """
        if promien <= 0:
            raise ValueError("Promień musi być większy od zera!")
        self.promien = promien

    def pole(self) -> float:
        """Zwraca pole koła."""
        return math.pi * self.promien ** 2

    def obwod(self) -> float:
        """Zwraca obwód koła."""
        return 2 * math.pi * self.promien
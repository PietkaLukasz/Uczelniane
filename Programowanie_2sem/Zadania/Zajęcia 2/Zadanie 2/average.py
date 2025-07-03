from typing import List

def average(numbers: List[float]) -> float:
    if not numbers:  # czy lista jest pusta czy nie
        return 0.0
    return sum(numbers) / len(numbers)
from typing import List


def find_average(numbers: List[int]) -> float:
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

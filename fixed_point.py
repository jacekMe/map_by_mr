"""Treść zadania:
Fixed point w tablicy to element, którego wartość jest równa jego indeksowi. Dostając na wejście tablicę elementów,
zwróć taką wartość, jeśli taki element równy indeksowi istnieje. W przeciwnym razie zwróć False. Podaj, jaka jest
złożoność pamięciowa i czasowa."""


from typing import List


def fixed_point(arr: List[int]):
    for index, value in enumerate(arr):
        if value == index:
            return value
        else:
            continue
    return False


if __name__ == "__main__":
    print(fixed_point([1, 5, 7, 8]))
    print(fixed_point([-10, -2, 2, 2, 2, 3, 4, 7, 9, 12, 13]))
    print(fixed_point([-6, 0, 40, 3]))

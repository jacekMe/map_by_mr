"""Sito Eratostenesa to algorytm używany do generowania wszystkich liczb pierwszych mniejszych niż N.
Metoda polega na wzięciu coraz większych liczb pierwszych i zaznaczeniu ich wielokrotności jako złożone.
Na przykład, aby znaleźć wszystkie liczby pierwsze mniejsze niż 100, najpierw zaznaczymy
[4, 6, 8, ...] (wielokrotności dwóch), następnie [6, 9, 12, ...] (wielokrotności trzech) i tak dalej.
Kiedy już mamy zrobić to dla wszystkich liczb pierwszych mniejszych niż N, nieoznaczone liczby, które pozostaną,
będą liczbą pierwszą.
Napisz algorytm, który wypisze pierwsze X takich liczb pierwszych."""

from typing import Generator, List


def sieve_eratosthenes(sieve: List[int] = []) -> List[int]:
    if sieve:       # sprawdzamy czy lista zawiera jakiekolwiek elementy
        length = len(sieve)
        sieve.extend([True for _ in range(length)])
    else:
        length = 10     # pczakujemy po 10 elementów
        sieve = [True for _ in range(length * 2)]
        sieve[0], sieve[1] = False, False   # 0 i 1 nie są liczbami pierwszymi

    # sieve generation
    for i in range(2, length):
        if sieve[i]:
            for j in range(2 * i, 2 * length, i): # trzeci parametr mówi o ile przeskoczyć ma pętla co iterację
                sieve[j] = False

    return sieve


def primes_gen() -> Generator[int, None, None]:
    primes = sieve_eratosthenes()       # uruchamiamy funkcję
    prev = 0
    while True:
        for i in range(prev, len(primes)):
            if primes[i]:
                yield i
        prev = len(primes)
        primes = sieve_eratosthenes(primes)


if __name__ == "__main__":
    gen = primes_gen()
    for _ in range(30):
        print(next(gen))

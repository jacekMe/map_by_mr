"""Treść zadania:
Napisz algorytm, który sprawdzi, czy numer PESEL jest poprawny.
Oblicz cyfrę kontrolną i jakiej płci jest osoba."""


def check_pesel(pesel):
    if len(pesel) == 11:
        numb = (int(pesel[0])) + (int(pesel[1]) * 3) + (int(pesel[2]) * 7) + (int(pesel[3]) * 9) + (int(pesel[4]))\
               + (int(pesel[5]) * 3) + (int(pesel[6]) * 7) + (int(pesel[7]) * 9) + (int(pesel[8])) + (int(pesel[9]) * 3)

        var = 10 - (numb % 10)
        if int(pesel[10]) == var and int(pesel[9]) % 2 == 0:
            return "Correct and female"
        else:
            return "Correct and male"

    return "Incorrect"


if __name__ == "__main__":
    print(check_pesel('111111'))
    print(check_pesel('62112861326'))
    print(check_pesel('62112861346'))
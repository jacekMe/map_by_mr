"""Przygotuj dwie funkcje, w których sprawdzisz poprawność adresu e-mail oraz poprawność wprowadzonego hasła. Mail
musi standardowo zawierać człon początkowy, znak małpy oraz domenę. Hasło musi mieć minimum 8 znaków, małe i duże
litery, minimum jedną cyfrę oraz minimum jeden znak specjalny.

Wejście
Do jednej funkcji adres e-mail, do drugiej hasło.

Wyjście
Informacja o tym, czy wprowadzona wartość jest poprawna czy nie."""
import re

regex_mail = "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
regex_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"

def check_mail(email):
    if re.fullmatch(regex_mail, email):
        print("Mail " + email + " jest poprawny")

    else:
        print("Mail " + email + " jest błędny")

def check_password(pwd):
    if re.fullmatch(regex_password, pwd):
        print("Hasło " + pwd + " jest poprawne")

    else:
        print("Hasło " + pwd + " jest błędne")

if __name__ == "__main__":
    mail = "test@gmail.com"
    check_mail(mail)

    mail = "jacekmeres@gmail.com"
    check_mail(mail)

    mail = "test.test.pl"
    check_mail(mail)


    print('-------------------------------------------------------')


    password = "test"
    check_password(password)

    password = "Pass1234"
    check_password(password)

    password = "P@Ssw0rD432#"
    check_password(password)

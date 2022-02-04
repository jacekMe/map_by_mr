"""Pewnego upalnego letniego dnia Tomek i jego przyjaciel Romek postanowili kupić arbuza. Wybrali największego i najdojrzalszego.
Następnie arbuz został zważony i waga pokazała pełne kilogramy.
Pospieszyli do domu, umierając z pragnienia i postanowili podzielić go, jednak stanęli przed trudnym problemem.
Tomek i Romek są wielkimi fanami parzystych liczb, dlatego chcą podzielić arbuza w taki sposób, aby każda z dwóch części ważyła parzystą liczbę kilogramów,
przy czym nie jest obowiązkowe, aby części były równe.
Chłopcy są bardzo zmęczeni i chcą jak najszybciej rozpocząć posiłek, dlatego warto im pomóc i przekonać się, czy potrafią podzielić arbuza tak, jak chcą.
Na pewno każdy z nich powinien otrzymać część dodatniej wagi."""

"""Wejście
Pierwszy (i jedyny) wiersz wejściowy zawiera liczbę całkowitą z zakresu od 1 do 100. Jest to waga arbuza kupionego przez chłopców.

Wyjście
Wypisz TAK, jeśli chłopcy potrafią podzielić arbuza na dwie części, z których każda waży parzystą liczbę kilogramów; i NIE w przeciwnym przypadku."""

kg = int(input())

if kg % 2 == 0 and 2 < kg < 101:
    print("TAK")
else:
    print("NIE")

### Opdracht
Schrijf een programma dat de determinant van een matrix berekent. De matrix kan bij deze oefening eender welke orde hebben.

Enkele opmerkingen bij deze (uitdagende) opgave:
- Maak gebruik van de methode met minoren en cofactoren.
- Maak gebruik van een recursieve functie die telkens de determeninant van de minor oproept. De recursie stopt wanneer hij een 2x2 minor tegenkomt, schrijf hier een aparte functie voor.
- Pas je functie *minor3x3()* aan zodat hij de minor uit een matrix van eender welke dimensies kan halen.
- Denk na over het teken van je minor, dit wordt bepaald door de indexen **uit de oorspronkelijke** matrix. Je zal deze op een of andere manier moeten meegeven doorheen je recursie (als extra argument, in een dictionary, ...?).

Succes!


### Voorbeeld

**Invoer:**

    2
    2
    1 2
    3 4

**Uitvoer:**

    -2

### Voorbeeld

**Invoer:**

    3
    3
    1 0 0
    0 1 0
    0 0 1

**Uitvoer:**

    1

### Voorbeeld

**Invoer:**

    6
    6
    1 2 3 4 5 6
    1 2 3 4 5 0
    1 2 3 4 0 0
    1 2 3 0 0 0
    1 2 0 0 0 0
    1 0 0 0 0 0

**Uitvoer:**

    -720




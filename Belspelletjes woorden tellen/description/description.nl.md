### Belspelletjes woorden tellen

*Dit is een eerste uitbreiding op de rekensleutel. De berekeningen uit de voorgaande opdrachten moeten nog steeds gelden!*

### Opdracht
Breid je programma uit zodat het **aantal woorden** in de opgave geteld wordt. Dit aantal wordt bij je totaal geteld.

Een woord beschouwen we hier als iets dat door spaties gescheiden wordt. De zin *"Los op: 1 + 2"* zou bijvoorbeeld 5 woorden tellen.


### Voorbeeld

**Invoer:**

    DRIE, TWEE, EEN, START! GEEF SNEL EEN BELLETJE! 100 - 100
    100 - 100

**Uitvoer:**

    18   <--- 0 (uitkomst berekening) + 7 (som verborgen cijfers) + 11 (aantal woorden)

### Tip
Denk goed na over wanneer je de invoer letter per letter *(gewone for loop)* of woord per woord *(met .split())* wil doorlopen.

### Belspelletjes: verborgen Romeinse cijfers

*Dit is een derde uitbreiding op de rekensleutel. De berekeningen uit de voorgaande opdrachten moeten nog steeds gelden!*

### Opdracht
Breid je programma uit zodat  **verborgen Romeinse cijfers** in de opgave geteld worden. Deze worden bij het totaal opgeteld.

Bijvoorbeeld: in de letter E zit zowel een Romeinse I(1) als een Romeinse L(50) verborgen. Tel zo ook de verborgen Romeinse cijfers in *E, L, D, A, P, F en T*.



### Voorbeeld

**Invoer:**

    DRIE, TWEE, EEN, START! GEEF SNEL EEN BELLETJE! 100 - 100
    100 - 100

**Uitvoer:**

    1346   <--- 0 (uitkomst berekening) + 6 (som verborgen cijfers) + 12 (aantal woorden) + 651 (Romeinse cijfers: D I L L L) 
                + 677 (verborgen Romeinse cijfers: DETEEEETATEEFELEEELLEE)

### Tip
Denk goed na over wanneer je de invoer letter per letter *(gewone for loop)* of woord per woord *(met .split())* wil doorlopen.

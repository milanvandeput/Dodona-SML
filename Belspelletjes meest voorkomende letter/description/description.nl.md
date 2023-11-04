### Belspelletjes: meest voorkomende letter

*Dit is een zesde uitbreiding op de rekensleutel. De berekeningen uit de voorgaande opdrachten moeten nog steeds gelden!*

### Opdracht
Breid je programma uit zodat de **de meest voorkomende letter** uit de opgave wordt gezocht. Het aantal keer dat deze letter voorkomt moet bij het totaal worden geteld.

**Opgelet:** We bedoelen hier enkel de 'echte' letter A, B, C, D, ..., Z. Dus geen cijfers of leestekens of spaties.



### Voorbeeld

**Invoer:**

    DRIE, TWEE, EEN, START! GEEF SNEL EEN BELLETJE! 100 - 100
    100 - 100

**Uitvoer:**

    1380  <--- 0 (uitkomst berekening) + 6 (som verborgen cijfers) + 12 (aantal woorden) + 651 (Romeinse cijfers: D I L L L) 
               + 677 (verborgen Romeinse cijfers: DETEEEETATEEFELEEELLEE) + 9 (langste woord BELLETJE!) + 12 (DRIE, TWEE, EEN, EEN, 100, 1, 0, 0, 100, 1, 0, 0)
               + 13  (de 'E' komt 13 keer voor)

### Tip
Voor elke letter een apart een lus schrijven die de tekst doorloopt om te tellen hoe vaak deze letter voorkomt is veel te veel werk. Maak daarom gebruik van een **lus in een lus**.

Maak gebruik van deze buitenste lus om alle letters af te gaan:
```python
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for x in ...: #binnenste lus
        ...

```

### Tip
Denk goed na over wanneer je de invoer letter per letter *(gewone for loop)* of woord per woord *(met .split())* wil doorlopen.

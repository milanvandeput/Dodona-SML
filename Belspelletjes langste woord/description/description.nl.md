### Belspelletjes: langste

*Dit is een vierde uitbreiding op de rekensleutel. De berekeningen uit de voorgaande opdrachten moeten nog steeds gelden!*

### Opdracht
Breid je programma uit zodat het **langste woord** uit de opgave wordt gezocht. Het aantal tekens van dit woord wordt bij het totaal geteld.

**Opgelet:** een punt of komma die aan een woord plakt, telt ook mee als teken. Bijvoorbeeld *BELLETJE!* is een woord van 9 tekens.



### Voorbeeld

**Invoer:**

    DRIE, TWEE, EEN, START! GEEF SNEL EEN BELLETJE! 100 - 100
    100 - 100

**Uitvoer:**

    1355  <--- 0 (uitkomst berekening) + 6 (som verborgen cijfers) + 12 (aantal woorden) + 651 (Romeinse cijfers: D I L L L) + 677 (verborgen Romeinse cijfers: DETEEEETATEEFELEEELLEE) + 9 (langste woord BELLETJE!)

### Tip
Je kan de lengte van een string nagaan met de functie *len()*

```python

len("hallo")     <---5
len("ha llo")    <---6
len("abcdefghijklmnopqrstuvwxyz")   <---26
```

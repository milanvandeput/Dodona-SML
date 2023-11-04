### Belspelletjes: aantal getallen

*Dit is een vijfde uitbreiding op de rekensleutel. De berekeningen uit de voorgaande opdrachten moeten nog steeds gelden!*

### Opdracht
Breid je programma uit zodat het **aantal getallen** uit de opgave telt. Dit aantal wordt bij het totaal geteld.

**Opgelet:** Je moet enkel de echte getallen tellen, zowel die in woorden als in cijfers geschreven staan. Romeinse cijfers tellen hier dus niet mee.

**Opgelet:** Het getal *100* in de opgave zal dus als 4 tellen. Want 100 is een getal maar 1, 0 en 0 zijn apart gelezen ook getallen. *We gaan niet zover dat we ook 10 en 00 gaan tellen.*


### Voorbeeld

**Invoer:**

    DRIE, TWEE, EEN, START! GEEF SNEL EEN BELLETJE! 100 - 100
    100 - 100

**Uitvoer:**

    1355  <--- 0 (uitkomst berekening) + 6 (som verborgen cijfers) + 12 (aantal woorden) + 651 (Romeinse cijfers: D I L L L) 
               + 677 (verborgen Romeinse cijfers: DETEEEETATEEFELEEELLEE) + 9 (langste woord BELLETJE!) + 12 (DRIE, TWEE, EEN, EEN, 100, 1, 0, 0, 100, 1, 0, 0)

### Tip
Nagaan of een variabele een getal is kan met de functie *.isdigit()*.
```python
var1 = "hallo"
var1.isdigit()    <--- False

var2 = "123"
var2.isdigit()   <---True

var3 = "hallo123"
var3.isdigit()   <---False
```

### Tip
Denk goed na over wanneer je de invoer letter per letter *(gewone for loop)* of woord per woord *(met .split())* wil doorlopen.

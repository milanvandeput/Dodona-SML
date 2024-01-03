### Matrices invoeren

We zullen doorheen deze lessen de matrices telkens op dezelfde manier door de gebruiker laten invoeren.

1. De gebruiker geeft het aantal rijen als input **m**.
2. De gebruiker geeft het aantal kolommen als input **n**.
3. De gebruiker geeft *m* keer een rij als string input.

*De code hieronder hoef je niet in detail te begrijpen (al is het niet onmogelijk). Je moet wel weten hoe het invoeren van de matrix werkt (zie hierboven).* 

```python
m = int(input("Hoeveel rijen bevat de matrix?"))
n = int(input("Hoeveel kolommen bevat de matrix?"))
matrix = []     
for i in range(m):
    rij_invoer = str(input("Geef de volgende rij"))
    rij_als_lijst = []
    for x in rij_invoer.split():
        rij_als_lijst.append(int(x))
    matrix.append(rij_als_lijst)
```

### Voorbeeld
**Invoer:**

    3
    4
    1 2 3 4
    5 6 7 8
    1 0 0 3

**Uitvoer:**

    #De code zelf produceert geen uitvoer.
    #De variabele *matrix* is nu: [[1,2,3,4],[5,6,7,8],[1 0 0 3]]

**Test de code zelf eens uit door een matrix naar keuze in te geven. Alle volgende opdrachten zullen vanuit deze code moeten starten.**
**Laat je ingevoerde matrices ook eens printen.**


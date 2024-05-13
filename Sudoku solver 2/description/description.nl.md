### Onze solver uitbreiden
Je maakte eerder al een programma *sudokusolver1(s)*. Nu heb je ook een functie geschreven die een controle op een blok kan uitvoeren. Deze gaan we toevoegen aan onze solver.

### Opdracht: getalzoeken2(s,m,n)
Kopieer je code van de eerdere functie *getalzoeken()*. Je moet twee zaken toevoegen aan deze functie: 

- Voeg ook een blokcontrole toe aan deze functie.
- Zorg dat de functie een *"."* returned indien er geen getal gevonden wordt.

Geef de functie de nieuwe naam *getalzoeken2()*.

```python
sudoku1 = [[9,".",".",".",6,1,2,8,"."],[2,6,8,".",".",4,7,".","."],[4,".",".",5,".",8,".",3,9],[".",8,".",2,5,".",1,4,"."],[".",".",4,8,1,".",".",9,3],[1,5,9,".",".",3,".",".",6],[5,".",2,".",".",7,4,".",8],[".",1,".",9,4,".",".",7,5],[".",4,7,1,8,".",9,".","."]]

def getalzoeken2(s,m,n):
    ...

```
### Voorbeeld
**Invoer:**

    getalzoeken(sudoku1,0,1)
    
**Uitvoer:**

    3

### Opdracht: sudokusolver2(s)
Kopieer je code van de eerdere functie *sudokusolver1()*. Je zal slecht 1 ding aan deze functie moeten aanpassen (denk maar eens na wat precies).

Geef de functie de nieuwe naam *sudokusolver2()*. Test je functie uit.


```python
sudoku0 = [[1,2,3,4,5,6,7,".",9],[2,".",4,5,6,7,8,9,1],[3,4,5,6,7,8,9,".",2],[4,5,".",7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]

def sudokusolver2(s):
    ...
```

### Voorbeeld
**Invoer:**

    sudokusolver2(sudoku1)
    
**Uitvoer:**

    [[9, 3, 5, 4, 6, 1, 2, 8, '.'], [2, 6, 8, 3, 9, 4, 7, 1, '.'], [4, 7, 1, 5, 2, 8, 6, 3, 9], [3, 8, 6, 2, 5, 9, 1, 4, 7], [7, 2, 4, 8, 1, 6, 5, 9, 3], [1, 5, 9, 7, '.', 3, 8, 2, 6], [5, 9, 2, 6, 3, 7, 4, '.', 8], [6, 1, 3, 9, 4, 2, '.', 7, 5], ['.', 4, 7, 1, 8, 5, 9, 6, 2]]

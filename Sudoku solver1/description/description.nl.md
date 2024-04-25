### Naar een eerste automatische solver...
Nu gaan we echt beginnen met een programma te schrijven dat de sudoku voor ons kan oplossen. We doen dit in twee stappen en schrijven de functies *getalzoeken(s,m,n)* en *sudokusolver1(s)*.

### Opdraht: getalzoeken(s,m,n)
Wat deze eerste functie doet is eenvoudig: het zoekt voor een gegeven plaats *(m,n)* in de sudoku *s* welk getal daar ingevuld mag worden. De functie returned dit getal. Onder een correct getal verstaan we een getal dat aan de rijcontrole en kolomcontrole voldoet. Je zal dus de functie *rijcontrole* en *kolomcontrole* hier moeten hergebruiken.

```python
sudoku0 = [[1,2,3,4,5,6,7,".",9],[2,".",4,5,6,7,8,9,1],[3,4,5,6,7,8,9,".",2],[4,5,".",7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]

def getalzoeken(s,m,n):
    ...
```
### Voorbeeld
**Invoer:**

    getalzoeken(sudoku0,0,7)
    
**Uitvoer:**

    8

### Opdracht: sudokusolver1(s)
De functie *sudokuvoler1(s)* is onze eerste versie van een volwaardige automatische sudoku-oplosser. De functie krijgt een sudoku *s* als input en zal de lege vakjes *'.'* invullen. Uiteraard zal hij hiervoor de functie *getalzoeken(s,m,n)* nodig hebben.

Een mogelijke opbouw van je code:

- Zoek doorheen de sudoku naar een lege plaats '.' .
- Zoek het getal dat op deze plaats mag ingevuld worden.
- Vul het getal in.
- Doorloop zo heel de sudoku.

```python
sudoku0 = [[1,2,3,4,5,6,7,".",9],[2,".",4,5,6,7,8,9,1],[3,4,5,6,7,8,9,".",2],[4,5,".",7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]

def sudokusolver1(s):
    ...
```

### Voorbeeld
**Invoer:**

    sudokusolver1(sudoku0)
    
**Uitvoer:**

    [[1,2,3,4,5,6,7,**8**,9],[2,'.',4,5,6,7,8,9,1],[3,4,5,6,7,8,9,**1**,2],[4,5,**6**,7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]



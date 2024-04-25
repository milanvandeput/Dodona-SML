### Sudoku rijcontrole
We starten met de eerste stap in het automatisch laten oplossen van een sudoku. We leren onze computer eerst om in een rij te controleren of een getal daar al in staat of niet. De code om dit te doen zetten we in een functie **rijcontrole(s,g,m,n)**. 

Deze functie heeft een aantal parameters:

- *s* is de sudoku
- *g* is het getal dat we willen laten controleren
- *m* is de rijindex
- *n* is de kolomindex

De functie returned de Booleaanse waarde *True* of *False*


### Opdracht: 
Schrijf de functie *rijcontrole(s,g,m,n)*.
```python
sudoku0 = [[1,2,3,4,5,6,7,".",9],[2,".",4,5,6,7,8,9,1],[3,4,5,6,7,8,9,".",2],[4,5,".",7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]

def rijcontrole(s,g,m,n):
    ...
```


### Voorbeeld
**Invoer:**

    rijcontrole(sudoku0,7,0,7)
**Uitvoer:**

    False

### Voorbeeld
**Invoer:**

    rijcontrole(sudoku0,8,0,7)
**Uitvoer:**

    True

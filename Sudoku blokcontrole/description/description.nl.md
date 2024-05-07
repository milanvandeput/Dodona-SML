### Sudoku blokcontrole
inleiding nieuwe sudoku1, print hem, zie je blok
```python
sudoku1 = [[9,".",".",".",6,1,2,8,"."],[2,6,8,".",".",4,7,".","."],[4,".",".",5,".",8,".",3,9],[".",8,".",2,5,".",1,4,"."],[".",".",4,8,1,".",".",9,3],[1,5,9,".",".",3,".",".",6],[5,".",2,".",".",7,4,".",8],[".",1,".",9,4,".",".",7,5],[".",4,7,1,8,".",9,".","."]]
```
functie **blokontrole(s,g,m,n)**. 

Deze functie heeft een aantal parameters:

- *s* is de sudoku
- *g* is het getal dat we willen laten controleren
- *m* is de rijindex
- *n* is de kolomindex

De functie returned de Booleaanse waarde *True* of *False*


### Opdracht: 
Schrijf de functie *blokcontrole(s,g,m,n)*.
```python
sudoku1 = [[1,2,3,4,5,6,7,".",9],[2,".",4,5,6,7,8,9,1],[3,4,5,6,7,8,9,".",2],[4,5,".",7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]

def blokcontrole(s,g,m,n):
    ...
```


### Voorbeeld
**Invoer:**

    blokcontrole()
**Uitvoer:**

    False

### Voorbeeld
**Invoer:**

    rijcontrole(sudoku0,8,0,7)
**Uitvoer:**

    True

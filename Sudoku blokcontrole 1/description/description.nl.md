### Sudoku blokcontrole 1
Onze vorige sudokusolver hield nog geen rekening met de 9 **blokken** in een sudoku. We gebruiken daarom vanaf nu een nieuwe (eenvoudige) sudoku: *sudoku1*.
```python
sudoku1 = [[9,".",".",".",6,1,2,8,"."],[2,6,8,".",".",4,7,".","."],[4,".",".",5,".",8,".",3,9],[".",8,".",2,5,".",1,4,"."],[".",".",4,8,1,".",".",9,3],[1,5,9,".",".",3,".",".",6],[5,".",2,".",".",7,4,".",8],[".",1,".",9,4,".",".",7,5],[".",4,7,1,8,".",9,".","."]]
```
*Laat de sudoku printen met je printsudoku() functie om een goed zicht te krijgen op deze sudoku.*


We hebben eerder al functies gemaakt die rijen en kolommen controleren. Nu maken we een gelijkaardige functie **blokcontrole(s,g,m,n)**. *In deze eerste versie is dit nog een vereenvoudige functie.*

Deze functie heeft een aantal parameters:

- *s* is de sudoku
- *g* is het getal dat we willen laten controleren
- *m* is de rijindex
- *n* is de kolomindex

De functie returned de Booleaanse waarde *True* of *False* die aangeeft of het gegeven getal op die plaats ingevuld mag worden.

*In deze eerste versie moet je enkel vakjes kunnen controleren die* **linksbovenaan** *in een blok staan.*


### Opdracht: 
Schrijf de functie *blokcontrole(s,g,m,n)*.
```python
sudoku1 = [[9,".",".",".",6,1,2,8,"."],[2,6,8,".",".",4,7,".","."],[4,".",".",5,".",8,".",3,9],[".",8,".",2,5,".",1,4,"."],[".",".",4,8,1,".",".",9,3],[1,5,9,".",".",3,".",".",6],[5,".",2,".",".",7,4,".",8],[".",1,".",9,4,".",".",7,5],[".",4,7,1,8,".",9,".","."]]

def blokcontrole(s,g,m,n):
    ...
```


### Voorbeeld
**Invoer:**

    blokcontrole(sudoku1,9,3,0)
    
**Uitvoer:**

    False

### Voorbeeld
**Invoer:**

    blokcontrole(sudoku1,8,3,0)
    
**Uitvoer:**

    False

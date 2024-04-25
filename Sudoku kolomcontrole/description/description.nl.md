### Sudoku kolomcontrole
Naast rijen willen we ook kolommen kunnen controleren. We maken dus op dezelfde wijze een functie **rijcontrole(s,g,m,n)** die de waarde *True* returned als het getal in deze kolom mag ingevuld worden en *False* als het niet mag ingevuld worden. 

### Opdracht: 
Schrijf de functie *kolomcontrole(s,g,m,n)*.
```python
sudoku0 = [[1,2,3,4,5,6,7,".",9],[2,".",4,5,6,7,8,9,1],[3,4,5,6,7,8,9,".",2],[4,5,".",7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]

def kolomcontrole(s,g,m,n):
    ...
```


### Voorbeeld
**Invoer:**

    kolomcontrole(sudoku0,3,1,1)
    
**Uitvoer:**

    True

### Voorbeeld
**Invoer:**

    kolomcontrole(sudoku0,1,1,1)
    
**Uitvoer:**

    False

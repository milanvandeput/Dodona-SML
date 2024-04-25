### Sudoku rijcontrole
We starten met de eerste stap in het automatisch laten oplossen van een sudoku. We leren onze computer eerst om in een rij te controleren of een getal daar al in staat of niet. De code om dit te doen zetten we in een functie **rijcontrole(s,g,i,j)**. Deze functie heeft een aantal parameters:

*e
*e
*e
*e

```python
sudoku0 = [[1,2,3,4,5,6,7,".",9],[2,".",4,5,6,7,8,9,1],[3,4,5,6,7,8,9,".",2],[4,5,".",7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]
```

Deze voorstelling van een sudoku is natuurlijk niet zo handig om te lezen. We wilen daarom allereerst een functie schrijven die de sudoku overzichtelijk rij per rij kan afprinten.
### Opdracht: een sudoku printen
Vul de volgende code aan om de sudoku rij per rij te laten printen
```python
def printsudoku(s):          #s is een 9x9 lijst
    for i in range("VUL AAN"):
        rij = ""
        for j in range("VUL AAN"):
            rij = rij+"VUL AAN"
        print("VUL AAN")
sudoku0 = [[1,2,3,4,5,6,7,".",9],[2,".",4,5,6,7,8,9,1],[3,4,5,6,7,8,9,".",2],[4,5,".",7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]
printsudoku(sudoku0)
```


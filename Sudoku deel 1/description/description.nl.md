### Sudoku
We gaan in de komende lessen een programma leren schrijven om een sudoku op te lossen. Dit is een complexe opgave dus we doen dit stap voor stap.

Een sudoku zal in python voorgesteld worden in een 9x9 lijst. Lege vakjes worden voorgesteld met een **.** . 
In de eerste lessen zullen we de oefeningen telkens uitvoeren op een heel eenvoudige sudoku: *sudoku0*:
```python
sudoku0 = [[1,2,3,4,5,6,7,".",9],[2,".",4,5,6,7,8,9,1],[3,4,5,6,7,8,9,".",2],[4,5,".",7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]
```

Deze voorstelling van een sudoku is natuurlijk niet zo handig om te lezen. We wilen daarom allereerst een functie schrijven die de sudoku overzichtelijk rij per rij kan afprinten.
### Opdracht: een sudoku printen
Vul de volgende code aan om de sudoku rij per rij te laten printen
```python
def printsudoku(s):          #s is een 9x9 lijst
    for i in range($vul aan$):
        rij = ""
        for j in range($vul aan$):
            rij = rij+$vul aan$
        print(rij)
sudoku0 = [[1,2,3,4,5,6,7,".",9],[2,".",4,5,6,7,8,9,1],[3,4,5,6,7,8,9,".",2],[4,5,".",7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]
printsudoku(sudoku0)
```


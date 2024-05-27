### Een nog betere solver?
Bekijk eens de resultaten van *sudokusolver2()*. Je zal merken dat sommige vakjes nog niet ingevuld zijn. Probeer ze zelf eens verder in te vullen: lukt dit? Denk eens na over hoe je de sovler 'slimmer' kan maken.

Probeer de volgende aanpassingen aan je code te maken. Doet dat in deze volgorde en **test je code uit na elke toevoeging.**
- ee
- ee



### Testen
Hier staan een aantal sudokus in oplopende moeilijkheid. Voeg de volgende code toe om je sudoku te laten testen:
TODO:nog andere testen zoeken!
``` python
sudokutestX = .... #hier je sudoku invoeren
sudoku_opgelost = sudokusolver3(sudokutestX)
print(sudoku_opgelost) #je kan ook de printsudokufunctie gebruiken om de sudoku zelf beter te zien
```
## sudokkutest 1
``` python
sudokutest1 = [
                [9,".",".",".",6,1,2,8,"."],
                [2,6,8,".",".",4,7,".","."],
                [4,".",".",5,".",8,".",3,9],
                [".",8,".",2,5,".",1,4,"."],
                [".",".",4,8,1,".",".",9,3],
                [1,5,9,".",".",3,".",".",6],
                [5,".",2,".",".",7,4,".",8],
                [".",1,".",9,4,".",".",7,5],
                [".",4,7,1,8,".",9,".","."]
                ]
```

## sudokutest 2
``` python
sudokutest2 = [
    [5, 3, ".", ".", 7, ".", ".", ".", "."],
    [6, ".", ".", 1, 9, 5, ".", ".", "."],
    [".", 9, 8, ".", ".", ".", ".", 6, "."],
    [8, ".", ".", ".", 6, ".", ".", ".", 3],
    [4, ".", ".", 8, ".", 3, ".", ".", 1],
    [7, ".", ".", ".", 2, ".", ".", ".", 6],
    [".", 6, ".", ".", ".", ".", 2, 8, "."],
    [".", ".", ".", 4, 1, 9, ".", ".", 5],
    [".", ".", ".", ".", 8, ".", ".", 7, 9]
]
```

## sudokutest 3
``` python
sudokutest3 = [
    [5, ".", ".", ".", 7, ".", ".", ".", "."],
    [6, ".", ".", 9, 1, 5, ".", ".", "."],
    [".", 1, 8, ".", ".", ".", ".", 6, "."],
    [8, ".", ".", ".", 6, ".", ".", ".", 3],
    [4, ".", ".", 8, ".", 3, ".", ".", 9],
    [7, ".", ".", ".", 2, ".", ".", ".", 6],
    [".", 6, ".", ".", ".", ".", 2, 8, "."],
    [".", ".", ".", 4, 9, 1, ".", ".", 5],
    [".", ".", ".", ".", 8, ".", ".", 7,1]
]

```





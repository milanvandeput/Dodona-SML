### Een nog betere solver?
Bekijk eens de resultaten van *sudokusolver2()*. Je zal merken dat sommige vakjes nog niet ingevuld zijn. Probeer ze zelf eens verder in te vullen: lukt dit? Denk eens na over hoe je de sovler 'slimmer' kan maken.

Enkele mogelijkheden:
- Laat de solver alleen een getal invullen wanneer dit de eneige mogelijkheid is.
- Laat de solver meerdere keren de sudoku doorlopen.
- Laat de solver eerst alle 1'en proberen invullen, dan de 2'en enz.
- Controleer ook de diagonalen?
- ...

... (nog aanvullen)

### Testen
Hier staan een aantal sudokus in oplopende moeilijkheid. Voeg de volgende code toe om je sudoku te laten testen:

``` python
sudokutestX = .... #hier je sudoku invoeren
sudoku_opgelost = sudokusolver3(sudokutestX)
print(sudoku_opgelost) #je kan ook de printsudokufunctie gebruiken om de sudoku zelf beter te zien
```
## sudokkutest 1
``` python
sudokutest1 = [
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





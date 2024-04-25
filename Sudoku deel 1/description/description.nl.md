### Sudoku
We gaan in de komende lessen een programma leren schrijven om een sudoku op te lossen. Dit is een complexe opgave dus we doen dit stap voor stap.


### Opdracht: een sudoku printen

´´´ python
sud = [[1,2,3,4,5,6,7,8,9],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],[4,5,6,7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]
def printsudoku(s):
    for i in range(9):
        rij = ""
        for j in range(9):
            rij = rij+" "+str(s[i][j])
        print(rij)
printsudoku(sud)
´´´


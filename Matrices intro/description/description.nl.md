### 2D lijsten

Matrices kunnen in Python voorgesteld worden als **lijsten van lijsten**. 

We nemen als voorbeeld de volgende 2x3 matrix:

<img width="100" alt="matrix" src="https://github.com/milanvandeput/Dodona-SML/assets/61200054/fa1d4c30-6cd1-4fe9-9774-af016747e1fa">

Deze kan in Python voorgesteld worden als een lijst met 2 elementen (=rijen), en elk element is een lijst van 3 elementen.

```python
matrix = [[1,2,3] , [4,5,6]]
```

Een rijmatrix of kolommatrix zien er dan als volgt uit:
```python
rijmatrix = [[1,2,3]] #de buitenste lijst bevat slechts 1 element (=rij), dit element is opnieuw een lijst.
kolommatrix = [[1],[2],[3]]   
```

### Matrices printen
We kunnen matrices printen met het gewone *print()* commando maar dit ziet er onoverzichtelijk uit:
```python
matrix = [[1,2,3] , [4,5,6]]
print(matrix)
```

Daarom is het aangeraden om elke rij op een aparte lijn te printen. Dit kan met een eenvoudige for-loop:
```python
matrix = [[1,2,3] , [4,5,6]]
for rij in matrix:
  print(rij)
```
### Elementen
Een element uit de i-de rij en de j-de kolom halen is eenvoudig, maar je moet 1 ding in het achterhoofd houden: **Python begint te tellen vanaf 0!**

Een element uit de i-de rij en de j-de kolom bekom je dus met het commando *matrix[i-1][j-1]*

Enkele voorbeeldjes:
```python
matrix = [[1,2,3] , [4,5,6]]
print(matrix[0][0])    --> 1
print(matrix[0][2])    --> 3
print(matrix[1][1])    --> 5
print(matrix[2][1])    --> error! Want deze matrix heeft maar 2 rijen.
```

### Dimensies
Om de dimensies van een matrix te achterhalen, kunnen we gebruikmaken van de functie *len()*. 

- len(matrix) geeft het aantal rijen weer *(want dit zijn het aantal elementen van de buitenste lijst)*.
- len(matrix[0]) geeft het aantal kolommen weer *(want dit zijn het aantal elementen van de eerste rij)*.

```python
matrix = [[1,2,3] , [4,5,6]]

m = len(matrix)
n = len(matrix[0])

print(m)
print(n)
```


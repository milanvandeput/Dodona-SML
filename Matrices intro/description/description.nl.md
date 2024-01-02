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
rijmatrix = [1,2,3]
kolommatrix = [[1] ,[2], [3]]   #elk element is opnieuw een lijst van 1 getal omdat er ook maar 1 getal staat op elke rij
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

### Dimensies
Kopieer onderstaande code en voer hem uit.

```python
print("Hello world")
```

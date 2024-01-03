### Matrices itereren

Stel dat we een matrix hebben ingevoerd (zoals in de vorige sectie uitgelegd) en we willen alle elementen van de matrix bekijken/aanpassen/controleren/... Dit kunnen we net zoals bij een lijst met een for-loop doen. Maar omdat een matrix een 2D lijst is, hebben we een **geneste for-loop** nodig. 
We zullen de variabelen *i* en *j* laten itereren over respectievelijk de rijen en kolommen.

*Test de volgende code eens uit om een zicht te krijgen op de volgorde waarin de elementen worden doorlopen.*
```python
m = int(input("Hoeveel rijen bevat de matrix?"))
n = int(input("Hoeveel kolommen bevat de matrix?"))
matrix = []     
for i in range(m):
    rij_invoer = str(input("Geef de volgende rij"))
    rij_als_lijst = []
    for x in rij_invoer.split():
        rij_als_lijst.append(int(x))
    matrix.append(rij_als_lijst)

for i in range(m):
    for j in range(n):
        print(matrix[i][j])
```

### Opdracht
Schrijf een (nutteloos) programma dat een matrix laat invoeren door de gebruiker, en alle elementen naar 0 verandert.
De matrix moet daarna ook rij per rij geprint worden.


### Voorbeeld

**Invoer:**

    2
    2
    1 2
    3 4

**Uitvoer:**

    0 0
    0 0

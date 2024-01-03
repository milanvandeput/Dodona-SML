### Opdracht
Schrijf een programma dat twee matrices vermenigvuldigt en het resultaat print. 
Enkele aandachtspunten:

- De gebruiker voert 2 matrices na elkaar in. Werk in je code dus bijvoorbeeld met *m1*, *n1*, *matrix1*,*m2*, *n2* en *matrix2*.
- Ga eerst na of de vermenigvuldiging mogelijk is. Indien niet, print je: Deze matrices kunnen niet vermenigvuldigd worden.
- Print het resultaat rij per rij.

**Belangrijk: je zal eerst een nulmatrix van de juiste dimensies moeten maken om het resultaat in op te slaan. Dit doe je met de volgende code:**
```python
resultaat = [ [0] * n for _ in range(m)] #hierbij is n het aantal kolommen en m het aantal rijen
```

### Voorbeeld

**Invoer:**

    2
    2
    1 2
    3 4
    2
    2
    5 6
    7 8

**Uitvoer:**

    [19, 22]
    [43, 50]

### Voorbeeld

**Invoer:**

    2
    2
    1 2
    3 4
    2
    3
    4 5 6
    7 8 9

**Uitvoer:**

    [18, 21, 24]
    [40, 47, 54]

**Invoer:**

    2
    3
    4 5 6
    7 8 9
    2
    2
    1 2
    3 4

**Uitvoer:**

    Deze matrices kunnen niet vermenigvuldigd worden.

### Tip
Dit is geen eenvoudige opgave. Werk eenvoudige voorbeeldjes eerst op papier uit. Bekijk het geval per geval: 2x2, 3x3, vierkante matrices, rechthoekige matrices...



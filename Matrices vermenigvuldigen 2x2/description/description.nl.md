### Opdracht
Schrijf een programma dat twee matrices vermenigvuldigt en het resultaat print. *We beperken ons hier tot 2x2 matrices.*
Enkele aandachtspunten:

- De gebruiker voert 2 matrices na elkaar in. Werk in je code dus bijvoorbeeld met *m1*, *n1*, *matrix1*,*m2*, *n2* en *matrix2*.
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
    4 5
    6 7

**Uitvoer:**

    [19, 22]
    [43, 50]

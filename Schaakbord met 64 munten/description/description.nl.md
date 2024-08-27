### Schaakbord met 64 munten
We programmeren in deze oefening de strategie die je hebt uitgedacht voor een schaakbord met 64 munten.

Het 8x8 bord wordt versimpeld voorgesteld als een *list* met 64 elementen. De munten op het bord zijn een *0* of een *1*.
```python
voorbeeldbord = [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
```
De locatie van de sleutel wordt aangeduid met de index van de *list*. Bij dit bord kan de sleutel dus 0 t.e.m. 64 zijn.

### Verstoppen
Schrijf een functie *verstoppen(bord,sleutel)* die één munten van het bord zal omdraaien. De functie returnet het aangepaste bord.
```python
def verstoppen(bord,sleutel):
    ...
    return(bordaangepast)
```

### Zoeken
Schrijf een functie *zoeken(bord)* die vanuit een bord kan aflezen waar de sleutel ligt. De functie returned de index van de sleutel.
```python
def zoeken(bord):
    ...
    return(sleutelindex)
```
### Testen
Je kan je code uiteraard in stukjes zelf testen. Om hem in Dodona te uit te testen, voeg je volgende code onderaan toe:

```python
def testen(bord,sleutel):
    bordnieuw=verstoppen(bord,sleutel)
    return(zoeken(bordnieuw))
```

### Voorbeeld
**Invoer:**

    testen([0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],20)
    
**Uitvoer:**

    20

...

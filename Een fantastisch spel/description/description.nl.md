### While lus
In deze laatste opdracht ga je een spel moeten programmeren. Typisch aan een spel is dat er verschillende beurten zijn en dat je op voorhand niet weet hoeveel beurten in totaal.

Een structuur om dit te programmeren in python is door gebruik te maken van een **while lus**. Hierbij wordt een **Booleaanse variabele** *'verdergaan'* op *True* gezet. Ergens in de lus moet er een if/else check zijn die bepaalt of het spel verdergaat (*verdergaan blijft True*) of dat het spel eindigt (*verdergaan wordt False*).

```python
verdergaan = True

while verdergaan:     #deze lus zal zich blijven herhalen zolang het spel verdergaat

    ...  #dingen die in een beurt van het spel gebeuren

    if ...:  #hier test je of het spel moet eindigen
        verdergaan = False  #de while lus zal zich niet meer herhalen
```

### Naam raden
Schrijf een programma om een spel mee te spelen waarbij je een naam (Joske) moet raden. Als je fout raadt wordt er "Het is fout!" geprint. Als je juist raadt wordt er "Het is juist!" geprint en stopt het programma.

Maak hiervoor gebruik van een structuur met een while-lus zoals hierboven beschreven.

### Voorbeeld
**Invoer:**

    Alexy
    Michele
    Sarah
    Joske
    
    
**Uitvoer:**

    Het is fout!
    Het is fout!
    Het is fout!
    Het is juist!

### Voorbeeld
**Invoer:**

    Joske
    
    
**Uitvoer:**

    Het is juist!




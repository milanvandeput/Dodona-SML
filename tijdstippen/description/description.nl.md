### Opdracht

Schrijf een programma die de verstreken tijd tussen twee tijdstippen van een digitale klok kan aflezen.
Het programma geeft als uitvoer eerst de verstreken uren en dan de verstreken minuten.

### Voorbeeld

**Invoer:**

    1010
    1540

**Uitvoer:**

    5
    30


### Voorbeeld

**Invoer:**

    1050
    1120

**Uitvoer:**

    0
    40

*Tip: laat de input als String inlezen en gebruik **string slicing** om de uren en minuten hieruit op te slaan in variabelen.*
*Een voorbeeldje:*
```python
string = "abcdefghijk"
eerste_letter = string[0]             #Uitkomst a, python begint vanaf 0 te tellen
derde_letter = string[2]              #uitkomst c
eerste_tot_derde_letter = string[0:2] #uitkomst abc
```

**Uitdaging:** Laat het programma ook werken wanneer het eerste tijdstip later is dan het tweede tijdstip. *Je kan hiervoor modulo gebruiken.* De laatste test checkt dit, maar dit telt als bonus en is niet vereist.


### Een mogelijke oplossingsmethode

*Deze methode is zeker niet de enige juiste methode, maar kan wel een leidraad zijn*

1. Haal de begin- en einduren en minuten uit de input. Gebruik string slicing (zie hierboven).
2. Bereken het totaal aantal verstreken minuten.
3. Gebruik modulo rekenen om het aantal verstreken uren en minuten te berekenen
4. Print je resultaten

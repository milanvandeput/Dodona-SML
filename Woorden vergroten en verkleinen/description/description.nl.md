### Opdracht()

Schrijf twee functies **woorden_vergroten()** en **woorden_verkleinen()** die de letters in een woord *(=string)* van hoofdletters naar kleine letters kunnen omzetten en omgekeerd.

*Om de functie niet nodeloos complex te maken, testen we enkel woorden met de eerste 5 letters van het alfabet.*

### Voorbeeld

**Invoer:**

    >>>woorden_verkleinen("ABC")

**Uitvoer:**

    abc

### Voorbeeld

**Invoer:**

    >>>woorden_vergroten("abc")

**Uitvoer:**

    ABC

### Tip
Met een **for loop** kan je alle letters in een woord afgaan.

In deze loop zal je letter per letter het nieuwe (verkleinde of vergrote) woord willen schrijven. Dit kan je doen door vooraf een **lege string** te definiëren. Letters toevoegen kan door de '+' bewerking.
```python
nieuw_woord = ""
nieuw_woord = nieuw_woord + "a"
```



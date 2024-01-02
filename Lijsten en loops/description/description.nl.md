### Lijsten en loops

We hebben al geleerd dat we via de index een bepaald element uit de lijst kunnen halen.

Om alle elementen van een lijst te doorlopen, gebruiken we een **for-loop**.

Voorbeeld 1: alle elementen uit een lijst printen
```python
lijst = [1,2,3,4,5,"hond","kat"]
for x in lijst:
    print(x)
```

Voorbeeld 2: alle elementen uit een lijst verdubbellen
```python
lijst = [1,2,3,4,5,"hond","kat"]
for x in lijst:
    print(2*x)
print(lijst)     #de lijst zelf is niet aangepast!
```

### Elementen aanpassen in de lijst

Er is ook een tweede methode, die gebruikt maakt van de **indexen**. Deze methode laat ons toe om elementen in de lijst aan te passen.

We gebruiken voor deze methode een **range() for-loop** die alle indexen afgaat. Hiervoor moeten we natuurlijk wel weten hoeveel elementen er in de lijst zitten. Dit kan eenvoudig met de functie **len()**.

Voorbeeld 3: alle elementen in een lijst verdubbellen en terug in de lijst zetten. 
```python
lijst = [1,2,3,4,5,"hond","kat"]
for i in range(len(lijst)):     #i zal nu alle getallen aannemen van 0 t.e.m. 6
    element = lijst[i]
    elementdubbel = 2*element
    lijst[i] = elementdubbel
print(lijst)    #de lijst is nu wel aangepast!
```

*Voor deze opdracht hoef je niks in te dienen.*

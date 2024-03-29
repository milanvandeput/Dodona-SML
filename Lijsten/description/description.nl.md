### Lijsten

We maken kennis met een nieuw datatype: **list**(lijst). Een lijst is een verzameling van geordende elementen. 

Een lijst wordt aangemaakt met de vierkante haakjes **[ ]**. De elementen worden gescheiden door een komma **,**

Voorbeeld: een lijst van getallen
```python
lijst1 = [1,2,3,5,2,10,4]
```
Voorbeeld: een lege lijst
```python
lijst2 = []
```

De elementen moeten geen natuurlijke getallen zijn, ze mogen van eender welk datatype zijn *(zelfs lijsten, hierover later meer)*.
```python
lijst3 = ["naam",20,3.01,"hello world",10]
```

### Elementen oproepen
Elementen in een lijst kunnen worden opgeroepen via hun **index**.

**Opgelet: in python beginnen we te tellen vanaf 0. Het eerste element is dus lijst[0]!** 

*Test onderstaande code uit bij 'code uitvoeren'*
```python
lijst1 = [1,2,3,5,2,"hond",4]
print(lijst1[0])
print(lijst1[1])
print(lijst1[5])
```
### Elementen aanpassen
Als je een element uit een lijst haalt en aanpast, zal dit in de lijst **ongewijzigd blijven**. Om elementen in de lijst aan te passen, moet je het terug toevoegen aan de lijst met behulp van zijn index.

```python
lijst = ["naam",20,3.01,"hello world",10]
element = lijst[0]
element = "achternaam"
print(lijst)   #de lijst zelf is ongewijzigd

lijst[0] = element
print(lijst)   #de lijst is nu wel gewijzigd
```

*Voor deze opdracht moet je niks indienen*

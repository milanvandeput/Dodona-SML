### Belspelletjes

[Belspelletjes](https://www.youtube.com/watch?v=LFLDU4Q9_Jk&t=31m18 "Basta belspelletjes")

Jullie gaan nu zelf een programma schrijven gelijkaardig aan dat van Gaetan *(de outfit met zonnebril en pet hoeft er niet bij).*

### Opdracht
Schrijf een programma dat de rekenspelletjes kan oplossen. In deze eerste versie moet het programma nog maar met 2 zaken rekening kunnen houden:

1. De berekening zelf moet uitgevoerd worden.
2. De verborgen cijfers moeten opgeteld worden *(bijvoorbeeld 8 in VANNACHT)*.

Om stap 1 te vergemakkelijken zal de invoer uit 2 delen bestaan. De volledige tekst en het rekendeel appart.  

### Voorbeeld

**Invoer:**

    VALT ER WEER WAT TE VIEREN VANAVOND? 10+20+30
    10+20+30
    
**Uitvoer:**
    64

### Tip: berekening 
Je kan in python een berekening rechtstreeks laten uitvoeren met de funcite *eval()*
```python
berekening = eval(1+2+3)
print(berekening) #uitkomst 6
```

### Tip: Tekst splitsen in woorden
Een tekst karakter per karakter doorlopen hebben jullie al leren doen met een *for loop (zie les 3)*. Maar om woorden te herkennen is het soms nuttig om de tekst woord per woord af te gaan (waarbij woorden gescheiden zijn met een spatie. Dit kan door de functie .split() toe te voegen.
```python
tekst = "Hallo, dit is een tekst."
for x in tekst.split()
    print(x)

==> uitvoer
    Hallo,
    dit
    is
    een
    tekst.
```
### Tip: woorden herkennen
Om te herkennen of een karakter voorkomt in een tekst, kan je een boolean maken met *in*.
```python
boolean1 = "boek" in "handboek"     #True
boolean2 = "boek" in "schoen"       #False
boolean3 = "ee" in   "er was eens een..."     #True
boolean4 = "aan" in "bijna anders"     #False

```




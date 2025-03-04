### Recursie
Recursieve functies zijn functies die zichzelf oproepen. 

We nemen als voorbeeld de functie *som(n)* die de som *1+2+3+4+...+n* berekent. Wanneer je dan bijvoorbeeld *som(7)* moet uitrekenen, kan je ook verwijzen naar het resultaat van *som(6)* en daar nog 7 bij optellen. Maar om op zijn beurt *som(6)* te berekenen, ga je kijken naar *som(5)* om daar 6 bij op te tellen.

Dit gaat zo door tot je uiteindelijk bij *som(0)* aankomt, wat gewoon 0 is. Dit *basisgeval* moet je apart onderscheiden bij een recursieve functie.

Hier is de code voor een recursieve functie *som(n)*:

```python
def som(n):
    if n == 0:  #basisgeval
        return 0
    else:
        return n + som(n - 1)
```

### Opdracht
In deze opdracht moet je opnieuw de functie *faculteit(n)* schrijven, maar deze keer moet het een recursieve functie zijn. Je moet dus ergens in je code *faculteit(n-1)* oproepen.

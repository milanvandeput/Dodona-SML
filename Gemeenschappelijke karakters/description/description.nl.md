### Opdracht

Schrijf een programma dat aan de gebruiker 2 woorden (of teksten) vraagt. Het programma print de **gemeenschappelijke karakters** die in beide woorden terugkomen.

**Opgelet:** Elk gemeenschappelijk karakter wordt slechts 1 keer geprint (ok al komt het in beide woorden meerdere keren voor). De karakters worden in 1 woord geprint.




### Voorbeeld

**Invoer:**

    brievenbus
    deurklink
    
**Uitvoer:**

    rienu

### Tip:
Je zal gebruik moeten maken van een derde string die aanvankelijk leeg is en waar doorheen de loop de gemeenschappelijke letters aan worden toegevoegd (nadat er nog eens is nagekeken of ze er al niet in voorkomen!).

```python
gemeenschappelijk = ""   #dit is een lege string

for ... :
    ...
        gemeenschappelijk = gemeenschappelijk + letter
```

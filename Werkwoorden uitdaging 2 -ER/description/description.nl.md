### Uitdaging 2: fouten verbeteren van werkwoorden op -ER 
Nu heb je al een aantal programma's geschreven die een werkwoord kunnen vervoegen. In deze oefening gaan we het omgekeerde doen: een vervoegd werkwoord controleren.

Schrijf een programma dat een persoonsvorm + vervoegd werkwoord als input vraagt. Het programma zegt eerst of de vervoeging juist/fout is. Indien fout, dan geeft het programma de juiste vervoeging.


**Tip:** Je kan een string splitsen met het commando *.split()*

```python
zin = "twee woorden"
zingesplitst=zin.split()
woord1=zingesplitst[0]
woord2=zingesplitst[1]
```


### Voorbeeld
**Invoer:**

    Je parles
    
**Uitvoer:**

    fout
    Je parle

### Voorbeeld
**Invoer:**

    Tu penses
    
**Uitvoer:**

    juist

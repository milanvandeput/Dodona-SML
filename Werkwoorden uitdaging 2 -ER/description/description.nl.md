### Uitdaging 2: fouten verbeteren van werkwoorden op -ER 
Nu heb je al een aantal programma's geschreven die een werkwoord kunnen vervoegen. In deze oefening gaan we het omgekeerde doen: een vervoegd werkwoord controleren.

Schrijf een programma dat een persoonsvorm + vervoegd werkwoord als input vraagt. Het programma zegt eerst of de vervoeging juist/fout is. Indien fout, dan geeft het programma de juiste vervoeging.

*Je mag er in deze oefening vanuitgaan dat alle werkwoorden van het basistype 'parler' zijn.*

**Tip:** Je kan een string splitsen met het commando *.split()*

```python
zin = "twee woorden"
zingesplitst=zin.split()
woord1=zingesplitst[0]
woord2=zingesplitst[1]
```

**Tip:** Je zal goed moeten nadenken over hoe je de stam en de uitgang onderscheid van elkaar.

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

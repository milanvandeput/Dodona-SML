### break
Het commando **break** statement kan gebruikt worden om een loop te verlaten. Alle volgende iteraties van de loop worden dus niet meer uitgevoerd. Vaak wordt een *break* statement voorafgegaan door een *if-statement* omdat je dit enkel in een bepaald geval wil doen.

```python
for letter in "woord":
  if letter == "r":
    break
  print(letter)


---uitvoer---
w
o
o
```

### continue
Het **continue** statement kan gebruikt worden om in een loop **één iteratie** over te slaan. Alle volgende iteraties van de loop worden wel nog uitgevoerd. Vaak wordt een *continue* statement voorafgegaan door een *if-statement* omdat je dit enkel in een bepaald geval wil doen.

```python
for letter in "woord":
  if letter == "r":
    continue
  print(letter)


---uitvoer---
w
o
o
d
```

Deze statements kunnen je code voerzichtelijker maken. Probeer ze eens toe te passen op een van de oefeningen die je al gemaakt hebt. Of ze gebruik ze in een van de volgende oefeningen.

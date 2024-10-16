### Loops met een string

Loops (of iteraties) worden gebruikt om een stuk code een aantal keer herhaaldelijk te laten uitvoeren.

Bij een **for loops met een string** wordt elk **teken** van de string afgegaan, en de code in de loop wordt een keer uitgevoerd.

*x is dus nu van het datatype String*

```python
for x in "woorden":
  print(x)

#uitvoer:
w
o
o
r
d
e
n
```

Een teken hoeft niet altijd een letter te zijn. Ook een spatie wordt gezien als een teken.
```python
for x in "hallo wereld      !":
  print(x)

#uitvoer:
h
a
l
l
o
 
w
e
r
e
l
d
 
 
 
 
 
 
!
```

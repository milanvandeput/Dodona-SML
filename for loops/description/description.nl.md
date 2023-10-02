### Loops

Loops (of iteraties) worden gebruikt om een stuk code een aantal keer herhaaldelijk te laten uitvoeren.

We zullen in deze les 3 soorten loops leren.

1. for loops met range()
2. for loops met een String
3. while loops 

### for loops met range()

Bij deze *range(n)* loops gebruik je een variabele x *(integer)* die je laat variëren tussen **0 en n-1**. 
In totaal wordt de code in de for loop dus n keer uitgevoerd!

```python
for x in range(10):
  print("hallo")

#uitvoer:
hallo
hallo
hallo
hallo
hallo
hallo
hallo
hallo
hallo
hallo
```

Je kan de variabele x zelf natuurlijk ook gebruiken in deze code. Zo krijg je telkens een andere uitvoer
```python
for x in range(10):
  print(2*x)

#uitvoer:
0
2
4
6
8
10
12
14
16
18
```

### for loops met een String

Een ander type for loops gebruikt een String waarbij er voor elk teken van de String, de code een keer wordt uitgevoerd.

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

*Het derde type loops, while loops, komt later aan bod.*

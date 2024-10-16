### Loops met range()

Loops (of iteraties) worden gebruikt om een stuk code een aantal keer herhaaldelijk te laten uitvoeren.

Hier leren we de **for loops met een range()** gebruiken.

Bij deze *range(n)* loops gebruik je een variabele x *(integer)* die je laat variëren tussen **0 en n-1**. 
In totaal wordt de code in de for loop dus n keer uitgevoerd.

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

Als je de loop wil laten beginnen bij een andere waarde dan 0, gebruik dan 2 parameters bij de range:
```python
for x in range(5,10):
  print(x)

#uitvoer:
5
6
7
8
9
```


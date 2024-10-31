### While loops

Naast de for loops bestaan er ook while loops.  Een while loop bestaat uit een voorwaarde *(Boolean)* en zolang deze voorwaarde voldaan *(True)* is, blijft de code in de loop zichzelf herhalen.


### Voorbeeld

```python
doorgaan = True   #Dit is een Booleaanse variabele

while doorgaan:
  print("hallo")

>>>uitvoer
hallo
hallo
hallo
hallo
hallo
hallo
hallo
hallo
hallo
...

```
Deze loop blijft eindeloos herhalen omdat de waarde van de variabele *doorgaan* op *True* blijft staan. Dit willen we natuurlijk niet. We moeten er daarom voor zorgen dat de variabele *doorgaan* ergens de kans krijgt om te veranderen naar *False*, bijvoorbeeld door een nieuwe input.

### Voorbeeld
```python
doorgaan = True   #Dit is een Booleaanse variabele

while doorgaan:
  print("hallo")
  vraag=input("Moet ik doorgaan? Ja/Nee")
  if vraag=="Ja":
    doorgaan=True
  else
    doorgaan=False

>>>uitvoer
hallo   ->input: Ja
hallo   ->input: Ja
hallo   ->input: Ja
hallo   ->input: Ja
hallo   ->input: Ja
hallo   ->input: Nee
...

```

### Voorbeeld

Een andere methode om while loops op tijd te doen stoppen is door een *teller* variabele in te voeren.

```python
t = 0   #dit is de teller variabele, voer deze in voor de loop!

while t<10:
  print(t)
  t=t+1

>>>uitvoer
0
1
2
3
4
5
6
7
8
9   
#hierna wordt t verhoogd tot 10, dus de loop zal niet nog eens uitgevoerd worden
```

Opgelet: de plaats in de code waar je de teller verhoogt, kan een andere uitvoer geven.
```python
t = 0   #dit is de teller variabele, voer deze in voor de loop!

while t<10:
  t=t+1
  print(t)
  
>>>uitvoer
1  #t wordt eerst verhoogd en dan geprint, dit geeft dus een andere uitkomst
2
3
4
5
6
7
8
9   
10  
```

### Wanneer gebruiken we een for-loop of een while-loop?

In principe kunnen alle codes die je moet een for-loop schrijft, ook met een while-loop geschreven worden en omgekeerd. Maar voor sommige programma's is de ene soort loop handiger om te gebruiken dan de andere.

  - **for-loops** gebruik je voor lussen waarvan je op voorhand weet hoe vaak ze zichzelf moeten herhalen.
  - **while-loops** gebruik je voor lussen waarvan je op voorhand niet weet hoe vaak ze zichzelf moeten herhalen.





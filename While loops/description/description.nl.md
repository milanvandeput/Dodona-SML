### While loops

Naast de for loops bestaan er ook while loops.  Een while loop bestaat uit een voorwaarde *(Boolean)* en zolang deze voorwaarde voldaan *(True)* is, blijft de code in de loop zichzelf herhalen.



### Voorbeeld

Een veelgebruikte methode om while loops te schrijven is door een *teller* variabele in te voeren.

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

### Voorbeeld
Je kan ook een Booleanse variabele invoeren die aanvankelijk *True* is maar doorheen de code *False* kan worden (en dan stopt de loop).

```python
voorwaarde = True   #dit is de Booleaanse variabele, voer deze in voor de loop!

while voorwaarde:
  antwoord = input("Moet de loop verder gaan?")
  if antwoord == "ja":
    print("de loop gaat verder")
  else:
    print("de loop stopt")
    voorwaarde = False

#test deze code zelf uit bij 'code uitvoeren'
 ```




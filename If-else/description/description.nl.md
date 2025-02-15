### If/else

Soms wil je dat een programma bepaalde code uitvoert in het ene geval, en andere code in een ander geval. Hiervoor maken we gebruik van de conditionele statements **if** en **else**.

Je maakt steeds gebruik van een boolean en het *if* statement gaat na of de waarde van deze boolean *True* of *False* is.
* Als de waarde *True* is zal de code in het blok onder *if* uitgevoerd worden.
* Als de waarde *False* is zal de code in het blok onder *else:* uitgevoerd worden.

### Voorbeeld

```python
var1 = True
if var1:
  print("iets")    #deze lijn zal uitgevoerd worden
else:
  print("iets anders")

var2 = False
if var2:
  print("iets")    
else:
  print("iets anders") #deze lijn zal uitgevoerd worden
```

Je hoeft niet met booleaanse variabelen te werken maar je kan ook rechtstreeks een vergelijking of ongelijkheid na het *if* statement plaatsen

```python
if 5>3:
  print("vijf is groter dan drie")   #deze lijn zal uitgevoerd worden 
else:
  print("vijf is niet groter dan drie")
```


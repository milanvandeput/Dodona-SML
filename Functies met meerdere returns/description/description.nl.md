### Functies met meerdere returns

We hebben al functies gezien met één of meerdere argumenten. Maar het is ook mogelijk om een functie meerdere variabelen te laten returnen. 

Voorbeeld: een functie die de som en het product van drie getallen *a*, *b* en *c* berekent:

``` python
def functie(a,b,c):
  som=a+b+c
  product=a*b*c
  return(som,product)
```

Hoe moet je deze functie dan oproepen? We testen dit uit met een *print* commando.

``` python
print(functie(1,3,3))

--> (7,9)
```

De functie returnet beide waarden terug in een *tuple*. Op deze datastructuur gaan we niet verder in.

Maar hoe kan je dan een specifieke waarde raadplegen? We maken gebruik van **indexen** zoals we dat ook bij lijsten doen.

``` python
print(functie(1,3,3)[0])

--> 7

print(functie(1,3,3)[1])

--> 9
```
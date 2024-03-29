### Functies

Functies kennen we uit de wiskundeles. Voor een bepaalde input *x*, berekent de functie een output, bijvoorbeeld *x²+x-1*.

Ook in Python bestaan er functies, maar deze kunnen veel meer dan enkel berekeningen doen. Een aantal functies kennen we al uit de voorbije lessen:

```python
print(x)  #deze functie print een variabele

int(x)  #deze functie verandert het datatype van x naar integer

round(x,y) #deze functie rondt het getal x af op y cijfers na de komma

```
Een functie bestaat uit een **naam**, bijvoorbeeld *print* en heeft geen/een/meerdere **parameters** als input tussen de haakjes, gescheiden door een komma. 

Soms moet een parameter van een bepaald **datatype** zijn. Bijvoorbeeld: de variabele y bij *round(x,y)* moet een natuurlijk getal zijn.

### Zelf functies maken

Python beschikt dus al over heel wat functies. Maar je kan ook zelf een **functie definiëren**.

Bijvoorbeeld: je wil zelf een functie maken die telkens 10 van een getal aftrekt.

```python
def tien_aftrekken(x):  #x moet dus een int of float zijn. Je hoeft niet met x te werken, dit mag eender welke naamgeving zijn.
  y = x-10
  return(y)             #return is de output die de functie teruggeeft
```
Kopieer deze code naar 'code uitvoeren'. Je zal merken dat de code geen uitvoer heeft. Dat komt omdat je enkel nog maar de functie hebt gedefiniëerd. Om een uitvoer te krijgen, moet je de functie ook **oproepen**.

Plak deze code er bijvoorbeeld achter:
```python
getal = tien_aftrekken(100)
print(getal)

getal2 = tien_aftrekken(getal)
print(getal2)

getal3 = tien_aftrekken(tien_aftrekken(getal))
print(getal3)
```




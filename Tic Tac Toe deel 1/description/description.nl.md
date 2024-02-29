### Opdracht
Schrijf een programma om het spelletje Tic Tac Toe mee te spelen. 

Je speelt Tic Tac Toe in een 3x3 veld. In het begin is dit veld nog leeg:
```python
veld = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
```
Het spelletje zal een aantal beurten duren, de speler kan telkens kiezen of hij nog wil verderspelen. Om dit te doen, geef je je code de volgende structuur:
```python
veld = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
print("Welkom bij Tic Tac Toe!")
doorgaan? = input("Wil je nog verderspelen? Ja/Nee")

while doorgaan?=="Ja":
  #Hier komt je code
  #
  #

  doorgaan = input("Wil je nog verderspelen? Ja/Nee")
```
### Opbouw van de code
Wat moet je allemaal in een beurt doen?

  1. Vraag de rijindex waar de speler een O wil toevoegen.
  2. Vraag de rijindex waar de speler een O wil toevoegen.
  3. Voeg de "O" toe in het veld.
  4. Print het veld rij per rij.
  5. Vraag de rijindex waar de speler een X wil toevoegen.
  6. Vraag de rijindex waar de speler een X wil toevoegen.
  7. Voeg de "X" toe in het veld.
  8. Print het veld rij per rij.
  9. Vraag of de speler verder wil spelen.

### Voorbeeld van een spelletje

Welkom bij Tic Tac Toe!


Wil je nog verderspelen? Ja/Nee

>>> Ja

In welke rij wil de speler een O toevoegen?

>>> 1

In welke kolom wil de speler een O toevoegen?

>>> 1

['O', ' ', ' ']

[' ', ' ', ' ']

[' ', ' ', ' ']

In welke rij wil de speler een X toevoegen?

>>> 2

In welke kolom wil de speler een X toevoegen?

>>> 1

['O', ' ', ' ']

['X ', ' ', ' ']

[' ', ' ', ' ']


Wil je nog verderspelen? Ja/Nee

>>> Ja

In welke rij wil de speler een O toevoegen?

>>> 2

In welke kolom wil de speler een O toevoegen?

>>> 3

['O', ' ', ' ']

['X', ' ', 'O']

[' ', ' ', ' ']

In welke rij wil de speler een X toevoegen?

>>> 3

In welke kolom wil de speler een X toevoegen?

>>> 1

['O', ' ', ' ']

['X ', ' ', 'O']

['X', ' ', ' ']


Wil je nog verderspelen? Ja/Nee
>>> Nee


### Belangrijk
Denk eraan dat in Python de indexen vanaf 0 worden geteld maar dat 'de speler' vanaf 1 zal tellen in zijn antwoorden.


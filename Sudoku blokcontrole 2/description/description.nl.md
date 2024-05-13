### Sudoku blokcontrole 2
In de vorige oefening heb je een functie geschreven die een blokcontrole kan uitvoeren, maar enkel op een getal uit de linkerbovenhoek van een blok. We willen dit natuurlijk kunnen testen van eender welk vakje. 

Je kan hiervoor een functie schrijven die voor alle 9 gevallen (linksboven, middenboven, rechtsboven, linksonder...) een andere test uitvoert. Maar dit is helemaal niet efficiënt. Daarom gaan we de volgende strategie toepassen:

- We laten onze functie de rij- en kolomindex afbeelden op die van de linkerbovenhoek uit het overeenkomstige blok.
- We laten onze eerder geschreven code een blokcontrole uitvoeren op het hele blok.

De moeilijkheid hierbij is natuurlijk de eerste stap. Hier is wat wiskundig denkwerk voor nodig...

### Opdracht:
Schrijf (op papier) een wiskundige functie die de rij- of kolomindex afbeeldt op die van de linkerbovenhoek. Enkele voorbeelden:

- rijindex 2 en kolomindex 8 worden afgebeeld op rijindex 0 en kolomindex 6.
- rijindex 7 en kolomindex 4 worden afgebeeld op rijindex 6 en kolomindex 3.
- rijindex 0 en kolomindex 0 worden afgebeeld op rijindex 0 en kolomindex 0.

*Tip: denk aan de modulo operators // en %.*

Test eventueel je functie uit in de sandbox.


### Opdracht: 
Schrijf de functie *blokcontrole2(s,g,m,n)*. Deze functie moet dus werken voor eender welke rij- en kolomindex.
```python
sudoku1 = [[1,2,3,4,5,6,7,".",9],[2,".",4,5,6,7,8,9,1],[3,4,5,6,7,8,9,".",2],[4,5,".",7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]

def blokcontrole2(s,g,m,n):
    ...
```


### Voorbeeld
**Invoer:**

    blokcontrole(sudoku1,9,0,1)
    
**Uitvoer:**

    False

### Voorbeeld
**Invoer:**

    blokcontrole(sudoku1,6,5,4)
    
**Uitvoer:**

    True

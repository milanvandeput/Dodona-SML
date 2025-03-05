Het **Binomium van Newton** (*kansrekenen hoofdstuk 2.2*) is een formule om veeltermen van de vorm $$(a+b)^n$$ uit te rekenen.

Enkele voorbeelden:
- $$(a+b)^2=a^2+2ab+b^2$$
- $$(a+b)^3=a^3+3a^2b+3ab^2+b^3$$
- $$(a+b)^4=a^4+4a^3b+6a^2b^2+4ab^3+b^4$$

Een oplettende lezer kan opmerken dat de coëfficiënten in de uitwerkingen van deze veeltermen overeenkomen met de getallen uit de driehoek van Pascal. De termen zijn dus allemaal van de vorm $$C^i_na^ib^{n-i}$$ waarbij *i* de macht is van *a*.

### Opdracht
Definiëer de functie *binomium(n,i)* die van de uitwerking van de veelterm $$(a+b)^n$$ de term van $$a^i$$ uitschrijft.

- Machten mogen geprint worden als a^2, a^3, ...
- Factoren met de macht *0* worden niet geprint.

**Tip:** werk met string *uitvoer* waar je de factoren om de beurt aan toevoegt met het commando *uitvoer = uitvoer + ...*

**Invoer:**

    >>>binomium(3,1)


**Uitvoer:**

    3a^2b
**Invoer:**

    >>>binomium(4,0)


**Uitvoer:**

    b^4


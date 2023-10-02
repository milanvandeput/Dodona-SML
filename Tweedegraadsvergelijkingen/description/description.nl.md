### Tweedegraadvergelijkingen

Tweedegraadsvergelijkingen zijn van de vorm

$$ax^2+bx+c=0$$

Je bepaalt de oplossingen met behulp van de discriminant

$$D = b^2 - 4ac$$

Bij een negatieve discriminant zijn er geen oplossingen.
Bij een positieve discriminant zijn er 2 oplossingen:

$$x_{12} = {{-b \pm \sqrt{D}}\over{2a}}$$

Bij een discriminant gelijk aan 0 is er 1 oplossing:

$$x  =  {{-b}\over{2a}}$$


### Opdracht
Schrijf een programma dat de oplossingen van een tweedegraadsvergelijking berekent. De inputs zijn de 3 coëfficiënten a, b en c. Met a $$\neq$$ 0.

Rond je oplossingen steeds af op 2 cijfers na de komma.

### Voorbeeld 1

**Invoer:**

    1
    4
    -5

**Uitvoer:**

    Er zijn 2 reële oplossingen: -5.0 en 1.0

### Voorbeeld 2

**Invoer:**

    1
    -12
    36

**Uitvoer:**

    Er is 1 reële oplossing: 6.0
    
### Voorbeeld 3

**Invoer:**

    4
    2
    7

**Uitvoer:**

    Er zijn geen reële oplossingen


### Tips bij deze oefeningen

Een vierkantswortel bereken je met de volgende code:

```python
import math #deze lijn komt helemaal bovenaan in je code

a = 4
wortel_a = math.sqrt(a) #uitkomst 2
```

**Maak eerst op papier een schema van je code. Welke gevallen wil je nagaan? Vermijd bijvoorbeeld dat je code de wortel van een negatieve discriminant moet berekenen.**

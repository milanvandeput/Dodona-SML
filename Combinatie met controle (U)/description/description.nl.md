Een groot onderdeel van het werk van programmeurs is om naast het schrijven van functies deze ook van een **invoercontrole** te voorzien. Dat betekent dat de functie ook moet werken bij een verkeerde invoer. De functie vermeldt dan wat de foute invoer is, en voert voor de rest geen code meer uit om mogelijke errors voor te zijn.

### Opdracht
In de vorige opdracht schreef je de functie *combinatie(n,p)*. Deze functie zou een error geven bij bijvoorbeeld de invoer *combinatie(5,-2)* omdat je geen faculteit van een negatief getal kan uitrekenen. Voorzie daarom deze functie nu van de volgende invoercontrole:

- p kan niet negatief zijn.
- n kan niet negatief zijn.
- n kan niet kleiner zijn dan p.

Denk eraan dat er ook meerdere fouten in één invoer kunnen zitten. De controleboodschappen worden dan (in bovenstaande volgorde) achter elkaar geprint.

**Invoer:**

    >>>combinatie(5,-2)


**Uitvoer:**

    p kan niet negatief zijn.

**Invoer:**

    >>>combinatie(-5,2)


**Uitvoer:**

    n kan niet negatief zijn. n kan niet kleiner zijn dan p.


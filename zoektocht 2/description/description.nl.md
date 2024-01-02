### Insert(), remove(),  pop(), sort()...

Er bestaan in Python nog veel meer handige commando's om lijsten aan te passen. Je kan een overzicht terugvinden in de **cheatsheet**.

Bijvoorbeeld: het commando *insert()* kan een element toevoegen op een plek naar keuze in de lijst.
```python
lijst = [1,2,3,4,5,6,7,8,9,10]
lijst.insert(3,"hallo")  #3 is de index, hallo is het nieuwe element
print(lijst)             ------> [1,2,3,"hallo",4,5,6,7,8,9,10]           
```

### Opdracht
Een nieuwe zoektocht! Volg de stappen en maak gebruik van de commando's in je cheatsheet.

```python
lijst = [311, 527, 349, 59, 811, 573, 951, 96, 583, 290, 122, 104, 975, 751, 675, 690, 805, 793, 719, 236, 993, 657, 658, 815, 644, 649, 772, 439, 55, 375, 365, 354, 465, 694, 982, 729, 943, 497, 440, 808, 939, 200, 913, 296, 12, 193, 610, 972, 549, 318, 892, 333, 273, 91, 468, 148, 927, 184, 172, 882, 249, 264, 773, 471, 143, 891, 411, 516, 392, 547, 125, 528, 415, 984, 430, 113, 376, 551, 771, 32, 433, 924, 323, 733, 900, 725, 232, 291, 339, 181, 739, 448, 985, 39, 187, 217, 71, 989, 34, 20, 699, 697, 403, 944, 360, 114, 221, 960, 511, 374, 679, 427, 359, 934, 355, 997, 621, 350, 409, 991, 589, 988, 737, 100, 761, 918, 534, 213, 784, 214, 362, 860, 301, 970, 270, 455, 736, 626, 505, 968, 716, 832, 872, 531, 399, 887, 552, 738, 540, 425, 29, 495, 41, 380, 118, 625, 962, 777, 596, 766, 469, 663, 105, 99, 275, 142, 178, 2, 760, 258, 554, 452, 18, 90, 52, 72, 203, 523, 328, 582, 58, 285, 919, 550, 330, 545, 6, 388, 225, 801, 205, 706, 648, 576, 653, 286, 763, 325, 16, 255]
```

1. Voeg het getal 0 toe op de 80e positie.
2. Sorteer de lijst van klein naar groot.
3. Verwijder de drie laatste elementen uit de lijst.
4. Sorteer de lijst van groot naar klein.
5. Haal het 197e getal uit de lijst
6. Print dit getal

### Matrices invoeren

We zullen doorheen deze lessen de matrices telkens op dezelfde manier door de gebruiker laten invoeren.

```python
r = 3
k = 4

matrix = []

for x in matrix:
    print(x)

for i in range(r):
    rij = str(input("geef de volgende rij"))
    lijstrij = []
    for x in rij.split():
        lijstrij.append(int(x))
    matrix.append(lijstrij)
```

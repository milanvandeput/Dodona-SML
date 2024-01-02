t1 = "1250"
t2 = "1120"

u1 = int(t1[0:2])
u2 = int(t2[0:2])
m1 = int(t1[2:4])
m2 = int(t2[2:4])

tv=(u2-u1)*60+(m2-m1)

uv = (tv//60 + 24)%24
mv = (tv%60 + 60)%60

print(uv)
print(mv)

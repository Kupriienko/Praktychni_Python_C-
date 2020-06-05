def d_add(a, b, s):
    if a + b <= s:
        rez = a + b
        return (rez, 0)
    else:
        rez = a + b - s
        return (rez, 1)

d = '25.6.2222'
dd=1
mm=2
yy=0
d_sp = d.split('.')
d_sp = list(map(int, d_sp))

d_sp[0], over = d_add(d_sp[0], dd, 31)
mm += over
d_sp[1], over = d_add(d_sp[1],mm,12)
yy += over
d_sp[2] += yy
d_sp = list(map(str,d_sp))

print(d_sp[0]+'.'+d_sp[1]+'.'+d_sp[2])
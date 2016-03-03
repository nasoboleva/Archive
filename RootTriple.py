//Корень кубического уравнения

s = input().split(" ")
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])

l = -2000
r = 2000

if a < 0:
    a = -a
    b = -b
    c = -c
    d = -d

while r - l > 0.000001:
    x = (l + r) / 2
    if (a * x * x * x) + (b * x * x) + (c * x) + d < 0:
        l = x
    else:
        r = x
        
print(x)        
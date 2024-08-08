import math
h, w = map(int, input().split(' '))

b = math.trunc((w/((h/100)**2)))

print(b)
if b > 25:
    print('Obesity')
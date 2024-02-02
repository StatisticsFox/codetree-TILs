n = int(input())
a=n
for j in range(n):
    for i in range(n):
        print(a, end = ' ')
        a -= 1
    print()
    a=n
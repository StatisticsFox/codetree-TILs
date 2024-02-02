n = int(input())

sv = 11
for i in range(n):
    row = []
    for j in range(n):
        row.append(sv)
        sv += 2
    
    for d in range(n):
        print(row[d], end = ' ')
    print()
    sv -= 2 * (n-1)
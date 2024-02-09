n, m = tuple(map(int, input().split()))

def min_eq(n, m):
    for i in range(max(n, m), (n*m)+1):
        if i%n==0 and i%m==0:
            print(i)
            break
            
min_eq(n, m)
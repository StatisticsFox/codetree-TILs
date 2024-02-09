n, m = tuple(map(int, input().split()))

def min_eq(n, m):
    for i in range(1, max(n, m)):
        h = min(n, m)
        if (h*i)%n==0 and (h*i)%m==0:
            print(h*i); break        
            
min_eq(n, m)
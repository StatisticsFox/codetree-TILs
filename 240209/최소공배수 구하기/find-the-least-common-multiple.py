# 최소 공배수가 두 수 a, b가 주어졌을때 a*b/최대공약수 인것만 알았어도..
n, m = tuple(map(int, input().split()))

def min_eq(n, m):
    for i in range(max(n, m), (n*m)+1):
        if i%n==0 and i%m==0:
            print(i)
            break
            
min_eq(n, m)
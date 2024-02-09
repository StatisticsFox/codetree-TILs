n, m = tuple(map(int, input().split()))

def get_div(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result


def 최대공약수(n, m):
    result = []
    h = abs(n-m)
    ll = get_div(h)
    for i in ll:
        if n%i == 0 and m%i==0:
            result.append(i)
    print(max(result))

최대공약수(n, m)
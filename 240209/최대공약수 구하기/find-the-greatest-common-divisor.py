# 유클리드 호제법을 이용해서 풀었는데 너무 좋지 않은 것 같다..
# 애초에 for문을 끝까지 다돌리면 gcd에 남는 것은 자동으로 최대공약수일탠데!!
n, m = tuple(map(int, input().split()))

def get_div(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result


def 최대공약수(n, m):
    if n == m:
        print(n)
    else:   
        result = []
        h = abs(n-m)
        ll = get_div(h)
        for i in ll:
            if n%i == 0 and m%i==0:
                result.append(i)
        print(max(result))

최대공약수(n, m)

## 이상적인 코드
# # 변수 선언 및 입력:
# n, m = tuple(map(int, input().split()))


# # n과 m의 최대공약수를 반환합니다.
# def find_gcd(n, m):
#     gcd = 0
#     for i in range(1, min(n, m) + 1):
#         if n % i == 0 and m % i == 0:
#             gcd = i

#     print(gcd)


# find_gcd(n, m)
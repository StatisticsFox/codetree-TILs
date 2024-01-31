n = int(input())
n_list = [i for i in range(1, n+1)]; n_list.reverse()
ans = []

for i in n_list:
    for j in n_list:
        ans.append((i, j))

for j in range(n):
    for i in range(n):
        print(ans[i], end=' ')
    print()
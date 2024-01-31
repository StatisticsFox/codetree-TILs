n = int(input())
n_list = [i for i in range(1, n+1)]; n_list.reverse()
ans = []

for i in n_list:
    for j in n_list:
        ans.append((i, j))

ans
for i in range(n):
    for j in range(n):
        print(f'({ans[i*n+j][0]},{ans[i*n+j][1]})', end=" ")
    print()
n = int(input())

def nnn(n):
    cnt = 1
    for i in range(n):
        for j in range(n):
            if cnt == 10:
                cnt = 1
                print(cnt, end = ' ')
                cnt += 1
            else:
                print(cnt, end = ' ')
                cnt += 1
        print()    
nnn(n)
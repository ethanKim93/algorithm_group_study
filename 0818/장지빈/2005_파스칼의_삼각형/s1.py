import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    a = int(input())
    print('#{}'.format(tc))
    if a == 1:
        print(1)
    else:
        ls = [[1], [1, 1]]

        for i in range(3, a+1):
            ls.append([0]*i)

        for x in range(len(ls)):
            ls[x][0] = 1
            ls[x][len(ls[x])-1] = 1

        for j in range(2, a):
            for k in range(1, j):
                ls[j][k] = ls[j-1][k-1] + ls[j-1][k]

        for _ in ls:
            print(*_)









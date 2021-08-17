import sys

sys.stdin = open('sample_input.txt', 'rt', encoding='UTF8')

T = int(input())
cnt = 0
result = 0
lst = []
lst2 = []
for i in range(0, T):
    N, M = map(int, input().split())
    for j in range(0, N):
        N2 = input()
        for k in range(0, len(N2)-1):
            if N2[k] == N2[len(N2) - k - 1]:
                cnt = 1
            elif N2[k] != N2[len(N2) - k - 1]:
                cnt = 2
                break
        if cnt == 1:
            result += 1
            print("{} {}".format(result, N2))
            cnt = 0
        elif cnt == 2:
            cnt = 0
        lst.append(N2)
    lst2.append(lst)
    lst = []
    print(" ")
for i in range(0, T):
    for j in range(0, len(lst2[i])):
        for k in range(0, len(lst2[i][j])):
            print(lst2[i][j][k])
            if lst2[i][j][k] == lst2[i][j][len(lst2[i][j]) - k - 1]:
                cnt = 1
            elif lst2[i][j][k] != lst2[i][j][len(lst2[i][j]) - k - 1]:
                cnt = 2
                break
        if cnt == 1:
            result += 1
            print("{} {}".format(result, lst2[i][j]))
            cnt = 0
        elif cnt == 2:
            cnt = 0



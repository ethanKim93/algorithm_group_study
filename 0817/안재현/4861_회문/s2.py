import sys

sys.stdin = open('sample_input.txt', 'rt', encoding='UTF8')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = []
    lst1 = []

    for _ in range(N):
        lst1.append(input())

    for i in range(N):  # 가로줄 탐색
        for j in range(N - M + 1):
            if lst1[i][j: j + M] == lst1[i][j: j + M][:: -1]:
                result.append(lst1[i][j: j + M])

    for i in range(N - M + 1):
        for j in range(N):
            lst2 = []  # 세로줄
            for k in range(M):
                lst2.append(lst1[i + k][j])
            if lst2 == lst2[:: -1]:
                result.append(''.join(lst2))

    print('#{} {}'.format(tc, result[0]))

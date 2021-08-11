import sys
sys.stdin = open('input.txt')


T = 10

for tc in range(1, T+1):
    box = [[0] * 100 for _ in range(100)]
    not_need = int(input())
    for x in range(100):
        box[x] = list(map(int, input().split()))
    sum = [0] * 202
    for i in range(100): #가로의 합
        for j in range(100):
            sum[i] += box[i][j]
    for j in range(100): #세로의 합
        for i in range(100):
            sum[100 + j] += box[i][j]
    for k in range(100): #대각선의 합
        sum[200] += box[k][k]
        sum[201] += box[k][99 - k]
    max_sum = sum[0]
    for s in range(len(sum)): # sum 비교
        if sum[s] > max_sum:
            max_sum = sum[s]
    print('#{} {}'.format(tc, max_sum))
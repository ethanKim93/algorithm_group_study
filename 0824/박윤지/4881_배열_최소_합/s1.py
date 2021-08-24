# 못풀겠다

import sys
sys.stdin = open('sample_input.txt')

def move(a, k, input):  # 행렬, k: 행 인덱스, input: N
    if k == input:
        pass
    else:
        for j in range(N):  # 특정 행에서 열 순회
            if arr[k][j]:
                selected.append(arr[k][j])
                move(a, k, input)

def cal(a, k, input):
    global order
    if k == input:
        sumV = sum(order)
        order = []
        return sumV
    else:
        for i in range(N):
            if i not in order:
                order.append(arr[k][i])
                k += 1
                cal(a, k, input)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 순열 구하기
    order = []
    print(cal(arr, 0, N))

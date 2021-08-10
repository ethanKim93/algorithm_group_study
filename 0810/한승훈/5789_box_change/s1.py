import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box_deco = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R): # 첫번째가 1이므로 수정함
            box_deco[j] = i

    print('#{}'.format(tc),end = ' ')
    print(*box_deco)


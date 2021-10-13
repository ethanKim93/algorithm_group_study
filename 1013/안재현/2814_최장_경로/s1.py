# 가지치기가 너무 많이 필요함. 다시 해야함
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    excel = [[]] * M
    if M == 0:
        print('#{} {}'.format(tc + 1, 1))
    else:
        for _ in range(M):
            arr = list(map(int, input().split()))
            switch = 0
            for i in range(M):
                empty = []
                if arr[0] not in excel[i] and arr[1] not in excel[i] and switch == 0:
                    empty.append(arr[0])
                    empty.append(arr[1])
                    switch = 1
                    excel.append(empty)
            print(excel)
        print('#{} {}'.format(tc + 1, arr))
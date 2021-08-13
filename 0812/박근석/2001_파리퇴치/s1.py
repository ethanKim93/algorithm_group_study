import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    list_a = [0]*N
    for i in range(N):
        list_a[i] = list(map(int, input().split()))
    # print(list_a)
    max_count = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            new_count = 0
            for k in range(M):
                for l in range(M):
                    new_count += list_a[i+k][j+l]
            if new_count > max_count:
                max_count = new_count

    print('#{} {}'.format(tc, max_count))
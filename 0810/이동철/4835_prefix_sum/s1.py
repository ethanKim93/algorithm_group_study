import sys
sys.stdin = open('input.txt')

T = int(input())
#테스트 케이스 개수 T가 주어진다.
for tc in range(1, T+1):
    N, M = map(int, input().split())
    #테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다
    ai = list(map(int, input().split()))
    #N개의 정수 ai가 주어진다.

    start = 0
    min_num = 9999999
    max_num = -9999999
    while True:
        total = 0
        if start + M > N:
            break
        for j in range(start, start + M):
            total += ai[j]
        if total > max_num:
            max_num = total
        if total < min_num:
            min_num = total
        start += 1

    print('#{} {}'.format(tc, max_num-min_num))
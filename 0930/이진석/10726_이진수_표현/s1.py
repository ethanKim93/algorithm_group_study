import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    bitN = (2**N) - 1                   # N개의 비트가 켜져있다는것은 2^N에서 1을 뺀것과 같은의미
    answer = 'OFF'
    if M & bitN == bitN:                # bitN의 모든 비트가 M에 포함되어 있을 때(마지막 N개의 비트가 모두 켜져있을 때)
        answer = 'ON'                   # ON
    print('#{} {}'.format(tc, answer))
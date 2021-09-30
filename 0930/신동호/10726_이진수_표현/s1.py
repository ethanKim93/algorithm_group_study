import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    switch = 2 ** N - 1 # 확인할 비트 부분 개수 만큼 111..1
    if M & switch == switch: # M에서 해당하는 부분이 전부 1이면 switch와 같아진다
        print('#{} ON'.format(tc))
    else:
        print('#{} OFF'.format(tc))
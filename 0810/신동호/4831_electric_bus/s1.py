import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    stops = list(map(int, input().split()))
    now = 0 #현재 정류장
    result = 0

    while not N <= now + K:
        sub = [stop for stop in stops if now < stop <= now + K] #현재 정류장 기준으로 갈 수 있는 정류장
        try:
            now = sub[-1] #정류장 업데이트
            result += 1
        except: #없으면 실패!
            result = 0
            break
    print('#{} {}'.format(tc, result))
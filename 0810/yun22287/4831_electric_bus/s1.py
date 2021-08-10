import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
		K, N, M = map(int, input().split())
# K, N, M 에 각 입력값 할당
# K = 충전 한 번에 갈 수 있는 정류장 수
# N = 종점인 정류장 번호
# M = 정류장 개수
    station = list(map(int, input().split())) + [N]
# 정류장 번호 리스트와 종점 정류장 번호를 station 에 할당
    a = 0
# 현재 위치 변수 a 초기화
    cnt = 0
# 충전 횟수 cnt 초기화
    n = K+1
# 이동하는 거리를 K+1로 초기화
    while a <= N: # a가 종점에 도달하기 전까지 반복
        n -= 1
        if a == N :
            cnt -= 1
            break
# a가 종점에 도달하면 마지막 한 번은 종점에서 충전한 것이라 횟수 하나 줄이고 반복 종료
        elif a + n in station:
            cnt += 1
            a += n
            n = K+1
# 현재 위치에서 n만큼 움직였을 때, 해당 위치가 정류장 번호 리스트에 존재한다면, 충전
        elif a + K < station[cnt] :
            cnt = 0
            break
# 현재 위치에서 K 만큼 움직였는데도, 다음 정류장 번호에 도달하지 못한다면, 종료
    print('#{0} {1}'.format(tc, cnt))
import sys
sys.stdin = open('input.txt')

def bus_count(bus_stop):    #버스가 들어오는지 여부 확인
    cnt = 0

    for i in range(N):  # N개의 노선
        if bus_route[i][0] <= bus_stop <= bus_route[i][1]: # 출발점 이상 / 종점 이하
            cnt += 1
    return cnt

# 1. 모든 노선 체크
for tc in range(1, int(input())+1):
    N = int(input()) # 버스 노선 수

    bus_route = []      # 버스의 노선들을 저장해놓을 리스트

    for i in range(N):
        A, B = map(int, input().split())
        bus_route.append((A, B))    #튜푸ㅡㄹ형태로 입력받은 A,B를  bus route로

    # 내가 확인하고 싶은 정류장의 개수
    P = int(input())
    ans = []        # 버스 수 저장할 리스트

    for i in range(P):
        C = int(input())
        ans.append(bus_count(C))

    print('#{}'.format(tc), end=' ')
    print(' '.join(map(str, ans)))
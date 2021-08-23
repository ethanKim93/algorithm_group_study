"""
T- 테스트 케이스 수
N -버스노선개수
P- 버스정류장개수
"""
import sys

sys.stdin = open('input.txt')


# 1. 모든 노선 체크
def bus_count(BusStop):
    cnt = 0
    for i in range(N):
        if BList[i][0] <= BusStop <= BList[i][1]:
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 버스 노선의 수

    BList = []  # 버스의 노선을 저장해 놓을 리스트

    for n in range(N):
        A, B = map(int, input().split())
        BList.append((A,B))


    # 확인 하고싶은 정류장의 개수
    P = int(input())
    Bus = []  # 버스 수를 저장해 놓을 리스트
    for i in range(P):
        C = int(input())
        Bus.append(bus_count(C))


    print(BList)
    print(Bus)


import sys
sys.stdin = open('input.txt')

# 1. 모든 노선 체크
for tc in range(1, int(input())+1):
    N = int(input()) # 버스 노선 수

    start = [0] * 5001      #1번부터 5000번정류장까지 사용하기 위해
    end = [0] * 5001        # 도착정류장
    bus_stop = [0] * 5001   #계산한 버스 표시

    for i in range(N):
        A, B = map(int, input().split())
        start[A] += 1
        end[B] += 1

    # 버스 계산
    for i in range(len(bus_stop)-1):
        bus_stop[i+1] = bus_stop[i] - end[i] + start[i+1]

    P = int(input())
    print('#{}'.format(tc), end=' ')
    for i in range(P):
        C = int(input())    #확인하고자 하는 정류장 번호
        print(bus_stop[C], end=' ')
    print()
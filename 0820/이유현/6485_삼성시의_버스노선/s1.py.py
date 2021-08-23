import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    route = []
    for i in range(N):
        ab = list(map(int, input().split()))
        route.append(ab)
    stop = []
    line = []
    
    P = int(input())
    for p in range(P):
        stop.append(int(input()))
        cnt = 0
        for r in route:
            if stop[-1] in range(r[0], r[1]+1):
                cnt += 1
        line.append(cnt)
    print('#{}'.format(tc), end=' ')
    for c in line:
        print(c, end=' ')
    print()



'''
N = 5 | 1 3 2 5 7 8 1 9 2 3
P = 5 | 1 2 3 4 5
(1) 모든 노선체크 ==> 2 4 4 2 2
(2) 정류장 미리 계산: 출발과 도착 인덱스를 만들고 정류장 계산
    출발 0 2 2 0 0 0 0 1 0 0 
    도착 0 0 0 2 0 1 0 0 1 1
    계산 0 2 4 4 2 2 1 2 2 1
    ==> 직전 버스 + 이번 출발 - 이전 도착
(3) 정류장 미리 계산2: 출발과 도착 범위 안에 들어가는 버스 카운팅
    버스 - 2 4 4 2 2 1 2 2 1
'''

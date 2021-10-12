import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    maps = list(map(int,input().split()))
    n = maps[0]
    maps = maps[1:]+[0] # 모든 충전소는 1이상 이므로, 0이 있으면 도착점

    if 0 in maps[0:maps[0]+1]: # 처음에 충전해서 갈 수 있으면
        print("#{} {}".format(tc, 0)) # 충전 안하고 도착 가능하므로 0

    else:
        i = cnt = 0 # i: 현재위치, cnt: 충전 횟수(답)
        flag = False # 주유소 방문 가능시 탈출할 flag
        while i < n: # 도착하기 전까지 반복
            mx = 0
            for x in range(i+1, i+maps[i]+1): # 현재위치 다음 곳부터 갈 수 있는 곳까지 탐색
                if x + maps[x] > mx: # 충전할 수 있는 최대 값 갱신
                    mx_idx = x
                    mx = maps[x]+x

                if 0 in maps[x:x+maps[x]+1]: # 0: 도착점, 도착점까지 갈 수 있으면 종료
                    cnt += 1
                    flag = True
                    break

            if flag:
                break
            else:
                cnt += 1
                i = mx_idx # 현재 위치를 충전할 정류장으로 이동


        print("#{} {}".format(tc,cnt))
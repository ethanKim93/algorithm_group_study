import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    k, n, m = map(int, input().split())  # 최대 이동거리: k, 목표: n, 충전소 갯수: m
    stations = list(map(int, input().split()))
    maps = [False] * (n + 1)

    for station in stations:
        maps[station] = True

    ans = cnt = start = 0  # 답: ans, 충전 횟수: cnt, 현재위치: start

    while True:
        flag = False  # 이동거리 안에 충전거리가 있나 없나 check = flag

        # 현재 위치 + 최대 이동거리로 목표까지 갈 수 있으면 끝
        if start + k >= n:
            ans = cnt
            break

        # 최대 이동거리만큼 뒤에서부터 check
        for i in range(start + k, start, -1):
            if maps[i]:
                start = i  # 충전소 찾으면 그 위치로 이동
                cnt += 1
                flag = True  # flag = 충전소 있다
                break

        # 최대 이동거리안에 충전소 없으면 break
        if not flag:
            break

    print("#{} {}".format(tc, ans))
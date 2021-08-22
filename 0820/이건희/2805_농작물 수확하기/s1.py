import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maps = [list(map(int, input())) for _ in range(n)]
    cnt = 1  # 시작점
    flag = False  # 최대점까지 갔는지 확인
    ans = []
    for i in range(n):
        ans.append(maps[i][n // 2 + 1 - cnt:n // 2 + cnt])  # 1부터 2만큼 늘어나도록

        if cnt == n // 2 + 1:  # 최대갯수에 도달하면 모드 전환
            flag = True

        if flag:  # 감소하는 모드
            cnt -= 1
        else:  # 증가하는 모드
            cnt += 1

    # 답 출력
    res = 0
    for i in ans:
        for x in i:
            res += x

    print("#{} {}".format(tc, res))
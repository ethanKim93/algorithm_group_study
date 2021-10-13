def team_maker(start=1, cnt=0):
    if cnt == N // 2:
        global min_score
        score = [0] * 2
        for i in range(N - 1):
            for j in range(i + 1, N):
                if team[i] == team[j]:
                    score[team[i]] += nums[i][j] + nums[j][i]
        if min_score > abs(score[0] - score[1]):
            min_score = abs(score[0] - score[1])
        return

    for i in range(start, N):
        if team[i] == 0:
            team[i] = 1
            team_maker(i + 1, cnt + 1)
            team[i] = 0


for case in range(int(input())):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    team = [0] * N
    min_score = 20000 * N
    team_maker()

    print("#{} {}".format(case + 1, min_score))

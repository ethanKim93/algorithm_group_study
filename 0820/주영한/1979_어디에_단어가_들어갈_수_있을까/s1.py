import sys
sys.stdin = open("input.txt")

def check_word(grid, N, target, dir = "row"):
    result = 0
    cnt = 0
    for i in range(N):
        # 기록을 할지 말지에 대한 상태를 check_point로 기록한다.
        check_point = True
        for j in range(N):
            # row에 대한 검사일 때
            if dir == "row":
                # 만약 해당하는 경우가 1일 경우에는 check_point를 False로 두고,
                # 0일 경우에는 check_point를 True로 둔다.
                if grid[i][j]:
                    check_point = False
                    cnt += 1
                else:
                    check_point = True

            # col에 대한 검사일 때
            else:
                if grid[j][i]:
                    check_point = False
                    cnt += 1
                else:
                    check_point = True

            # 행 또는 열의 마지막 원소를 검사할때는 check_point를 True로 두어
            # 체크가 될 수 있게 한다.
            if j == N-1 :
                check_point = True

            # check_point가 True인 경우,
            # 즉 마지막 원소를 보고 있거나, 1에서 0으로 바뀌었을 때, 0을 보고있을때
            # 상태를 체크한다.
            if check_point:
                # 연속되는 1이 target(K) 와 같을 경우 result를 증가시킨다.
                if cnt == target:
                    result += 1
                cnt = 0

    return result


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    # 주어진 입력에 대한 단어 퍼즐을 정의함
    grid = [0] * N
    for row in range(N):
        grid[row] = list(map(int, input().split()))

    cnt = check_word(grid, N, K, "row") + check_word(grid, N, K, "col")

    print("#{} {}".format(tc, cnt))
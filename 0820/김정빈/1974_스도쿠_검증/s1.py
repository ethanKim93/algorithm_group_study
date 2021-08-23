#1974. 스토쿠 검증
T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1

    #행열 체크
    for i in range(9):
        rcheck = [0] * 9
        ccheck = [0] * 9
        for j in range(9):
            rcheck[arr[i][j] - 1] += 1
            ccheck[arr[j][i] - 1] += 1
        if 0 in rcheck or 0 in ccheck: #0이 있으면 겹치는 수가 있다는 뜻
            ans = 0

    # 3*3 체크
    for i in range(0,7,3):
        for j in range(0,7,3):
            cross = [0] * 9
            for y in range(3):
                for x in range(3):
                    cross[arr[i+y][i+x]-1] += 1
        if 0 in cross:
            ans = 0

    print('#{} {}'.format(tc, ans))
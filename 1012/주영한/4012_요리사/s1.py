def getFlavor():
    global combinations
    flavor_0 = 0
    flavor_1 = 0
    for row in range(N):
        for col in range(N):
            if combinations[row] == 0 and combinations[col] == 0:
                flavor_0 += table[row][col]
            if combinations[row] == 1 and combinations[col] == 1:
                flavor_1 += table[row][col]
    result = flavor_1 - flavor_0 if flavor_1 > flavor_0 else flavor_0 - flavor_1
    return result

def backtracking(cnt, pos):
    global min_gap, combinations
    if cnt == N // 2:
        temp_num = getFlavor()
        if min_gap > temp_num:
            min_gap = temp_num
        return
    
    if N - pos < N // 2 - cnt:
        return

    combinations[pos] = 1
    backtracking(cnt + 1, pos + 1)
    combinations[pos] = 0
    backtracking(cnt, pos + 1)
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    combinations = [0] * N
    min_gap = 20000 * 8
    backtracking(0, 0)
    print("#{} {}".format(tc, min_gap))
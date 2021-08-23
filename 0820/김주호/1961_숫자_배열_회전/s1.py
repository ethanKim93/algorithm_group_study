import copy

T = int(input())

for case in range(T):
    N = int(input())
    li = [[0]] * N
    rot_li = []
    total_li = []
    for rep in range(N):
        li[rep] = list(map(int, input().split()))
        rot_li.append([0] * N)
        total_li.append([] * N)
    for rot in range(3):
        for col in range(N):
            for row in range(N):
                rot_li[col][N - row - 1] = li[row][col]
            total_li[col].append("".join(map(str, rot_li[col])))
        li = copy.deepcopy(rot_li)
    print(f"#{case + 1}")
    for again in range(N):
        print(" ".join(map(str,total_li[again])))
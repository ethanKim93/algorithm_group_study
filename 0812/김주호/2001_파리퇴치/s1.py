import sys
sys.stdin = open("input.txt")

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    li = []
    for _ in range(N):
        li.append(list(map(int, input().split())))

    max_fly = 0
    for row in range(N - M + 1):
        for col in range(N - M + 1):
            fly = 0
            for row_adder in range(M):
                for col_adder in range(M):
                    fly += li[row + row_adder][col + col_adder]

            if max_fly < fly:
                max_fly = fly

    print("#{} {}".format(case + 1, max_fly))
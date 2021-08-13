import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for case in range(T):
    li = [[0] * 10 for _ in range(10)]
    N = int(input())
    total = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for row in range(r1, r2 + 1):
            for col in range(c1, c2 + 1):
                if li[row][col] != color:
                    li[row][col] += color

    for row in range(10):
        for col in range(10):
            if li[row][col] >= 3:
                total += 1

    print("#{} {}".format(case + 1, total))
import sys
sys.stdin = open('sample_input.txt')


for case in range(int(input())):
    N = int(input())
    plan = [list(map(int, input().split())) for _ in range(N)]

    plan.sort(key=lambda p: p[1])
    print(plan)

    total = 0
    time = 0
    for s, e in plan:
        if time <= s:
            total += 1
            time = e

    print("#{} {}".format(case + 1, total))
import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    rooms = [0] * 201
    for _ in range(N):
        now, goal = map(int, input().split())
        if now > goal:
            now, goal = goal, now
        if now % 2:
            now += 1
        if goal % 2:
            goal += 1
        now, goal = now // 2, goal // 2
        for i in range(now, goal+1):
            rooms[i] += 1
    route = 0
    for j in rooms:
        if j > route:
            route = j

    print('#{} {}'.format(tc, route))

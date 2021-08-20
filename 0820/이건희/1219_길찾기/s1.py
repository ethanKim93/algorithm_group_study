import sys

sys.stdin = open("input.txt")

for _ in range(1, 11):
    tc, n = map(int, input().split())
    road = list(map(int, input().split()))

    ch1 = [0] * 100
    ch2 = [0] * 100

    for i in range(n):
        if ch1[road[2*i]] == 0:
            ch1[[road[2*i]] = road[2*i+1]
        else:
            ch2[[road[2*i]]] = road[2*i+1]


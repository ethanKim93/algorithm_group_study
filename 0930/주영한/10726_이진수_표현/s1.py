import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    flag = "ON"
    for idx in range(N):
        if M & (1 << idx):
            continue
        flag = "OFF"
    print("#{} {}".format(tc, flag))
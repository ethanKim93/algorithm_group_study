import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    word = list(input())
    temps = {}
    text = list(input())
    mx = 0

    for i in word:
        temps[i] = 0

    for i in text:
        if i in temps:
            temps[i] += 1

    for i in temps.values():
        if i > mx:
            mx = i

    print("#{} {}".format(tc, mx))
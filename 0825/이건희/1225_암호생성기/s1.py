import sys

sys.stdin = open("input.txt")

for i in range(10):
    tc = int(input())
    maps = list(map(int, input().split()))
    start = 1
    while True:
        pos = maps.pop(0)
        if pos - start <= 0:
            pos = 0
            maps.append(pos)
            break

        else:
            pos -= start
            maps.append(pos)
            start = (start % 5) + 1

    print("#" + str(tc), end=" ")
    print(*maps)

import sys

sys.stdin = open("input.txt")


def RSP(new_start, new_end):
    player1 = maps[new_start]
    player2 = maps[new_end]
    if player1 == rules[(player1, player2)]:
        return new_start
    elif player2 == rules[(player1, player2)]:
        return new_end
    else:
        return new_start


def match(start, end):
    if start == end:
        return start

    mid = (start + end) // 2
    new_start = match(start, mid)
    new_end = match(mid + 1, end)
    return RSP(new_start, new_end)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maps = list(map(int, input().split()))
    rules = {(1, 2): 2, (2, 3): 3, (1, 3): 1, (3, 1): 1, (3, 2): 3, (2, 1): 2, (1, 1): 0, (2, 2): 0, (3, 3): 0}

    print("#{} {}".format(tc, match(0, n - 1) + 1))

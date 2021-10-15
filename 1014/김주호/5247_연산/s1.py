from collections import deque


def add(val, s):
    if 0 <= val <= 1000000 and check[val]:
        check[val] = False
        queue.append((val, s + 1))


for case in range(int(input())):
    A, B = map(int, input().split())

    check = [True] * 1000001
    queue = deque()
    queue.append((B, 0))
    min_cnt = 1000001

    while queue:
        now, step = queue.popleft()
        if now <= A:
                min_cnt = min((A - now) // 10 + (A - now) % 10 + step, min_cnt)
        else:
            add(now + 10, step)
            if now % 2:
                add(now + 1, step)
                add(now - 1, step)
            else:
                add(now // 2, step)

    print("#{} {}".format(case + 1, min_cnt))

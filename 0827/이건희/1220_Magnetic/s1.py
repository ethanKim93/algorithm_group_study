# 1
import sys

sys.stdin = open("input.txt")

for tc in range(1,11):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    for c in range(n):
        stack = []
        for r in range(n):
            if maps[r][c] != 0:
                stack.append(maps[r][c])

        while stack:
            # 앞에 N(1), 뒤에 S(2)
            if stack[0] == 2:
                stack.pop(0)
            elif stack[-1] == 1:
                stack.pop()
            else:
                break

        flag = False
        while stack:
            checking = stack.pop()
            if checking == 2:
                flag = True
            else:
                if flag:
                    cnt += 1
                    flag = False

    print("#{} {}".format(tc, cnt))


# 2
for tc in range(1,11):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    for c in range(n):
        flag = False
        for r in range(n):
            if maps[r][c] == 1:
                flag = True
            else:
                if maps[r][c] == 2 and flag:
                    flag = False
                    cnt += 1

    print("#{} {}".format(tc, cnt))
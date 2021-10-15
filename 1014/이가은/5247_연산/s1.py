# 제한시간 초과...
import sys
sys.stdin = open('sample_input.txt')

def bfs():
    global result

    while queue:
        num1, cnt = queue.pop(0)
        if num1 == M:
            result = cnt
            return

        for i in range(4):
            num2 = 0
            if i == 0 :
                num2 = num1 * 2

            elif i == 1:
                num2 = num1 + 1

            elif i == 2:
                num2 = num1 - 1

            elif i == 3:
                num2 = num1 - 10

            if 0 < num2 <= A:
                if num2 not in check:
                    check.append(num2)
                    queue.append((num2, cnt + 1))


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())

    A = 1000000
    check = []
    queue = []
    queue.append((N, 0))
    result = 0

    bfs()
    print('#{} {}'.format(tc, result))

import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = 10

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    stack = [[] for _ in range(100)]
    result = 0
    for i in range(100):
        for j in range(100):
            if matrix[i][j] == 1:
                stack[j].append(1)
            if matrix[i][j] == 2:
                stack[j].append(2)
    for k in range(100):
        while stack[k] and stack[k][0] == 2:
            stack[k].pop(0)
        while stack[k] and stack[k][-1] == 1:
            stack[k].pop()
        if stack[k]:
            for s in range(1, len(stack[k])):
                if stack[k][s] == (stack[k][s-1]+1):
                    result += 1
    print('#{} {}'.format(tc, result))

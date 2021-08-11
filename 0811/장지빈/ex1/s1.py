import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = int(input())

idxX = [0, 1, 0, -1]
idxY = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    newone = [[0 for _ in range(5)] for __ in range(5)]

    for i in range(len(li)):
        for j in range(len(li[0])):


    # pprint(li)
    #
    # for i in range(len(li)):
    #     for j in range(len(li[0])):
    #         if i == 0:
    #             if j == 0:
    #                 li[i][j] = abs(li[i+1][j] - li[i][j]) + abs(li[i][j+1] - li[i][j])
    #                 break
    #             elif j == 4:
    #                 li[i][j] = abs(li[i+1][j] - li[i][j]) + abs(li[i][j-1] - li[i][j])
    #                 break
    #             else:
    #                 li[i][j] = abs(li[i + 1][j] - li[i][j]) + abs(li[i][j - 1] - li[i][j]) + abs(li[i][j + 1] - li[i][j])
    #                 break
    #         elif i == 4:
    #             if j == 0:
    #                 li[i][j] = abs(li[i - 1][j] - li[i][j]) + abs(li[i][j + 1] - li[i][j])
    #                 break
    #             elif j == 4:
    #                 li[i][j] = abs(li[i - 1][j] - li[i][j]) + abs(li[i][j - 1] - li[i][j])
    #                 break
    #             else:
    #                 li[i][j] = abs(li[i - 1][j] - li[i][j]) + abs(li[i][j - 1] - li[i][j]) + abs(li[i][j + 1] - li[i][j])
    #                 break
    #         elif j == 0:
    #             if i == 1 or i == 2 or i == 3:
    #                 li[i][j] = abs(li[i - 1][j] - li[i][j]) + abs(li[i][j + 1] - li[i][j]) + abs(li[i][i + 1] - li[i][j])
    #                 break
    #         elif j == 4:
    #             if i == 1 or i == 2 or i == 3:
    #                 li[i][j] = abs(li[i - 1][j] - li[i][j]) + abs(li[i][j - 1] - li[i][j]) + abs(li[i][i + 1] - li[i][j])
    #                 break
    #         else:
    #             li[i][j] = abs(li[i - 1][j] - li[i][j]) + abs(li[i][j - 1] - li[i][j]) + abs(li[i + 1][j] - li[i][j]) + abs(li[i][j + 1] - li[i][j])
    #
    # pprint(li)
    # total = 0
    # for x in range(len(li)):
    #     for y in range(len(li[0])):
    #         total += li[x][y]
    # print(total)
import sys
sys.stdin = open('input.txt')
from pprint import pprint

# def comb(Nn):
#     global combination
#     for i in range(1 << len(Nn)):
#         tmp = []
#         for j in range(len(Nn)):
#             if i & (1 << j):
#                 tmp.append(Nn[j])
#         combination.append[tmp[0]]
#     return

def synergy(li1, li2):
    global ans
    if li1[0] == li2[0] or li1[0] == li2[1] or li1[1] == li2[0] or li1[1] == li2[2]:
        return
    food1, food2 = matrix[li1[0]][li1[1]] + matrix[li1[2]][li1[3]], matrix[li2[0]][li2[1]] + matrix[li2[2]][li2[3]]
    syn = abs(food1 - food2)
    if syn >= ans:
        return
    else:
        ans = syn
        return
def check():
    global ans

for tc in range(1, int(input())+1):
    ans = 987564321
    N = int(input())
    n = N//2
    Nn = [i for i in range(1, n+1)]
    matrix = [list(map(int, input().split())) for _ in range(N)]
    combination = []
    for i in range(N):
        for j in range(i+1, N):
            combination.append([i, j, j, i])
    for i in range(len(combination)-1):
        for j in range(i+1, len(combination)):
            synergy(combination[i], combination[j])
    # pprint(matrix)
    print(combination)

    print('#{} {}'.format(tc, ans))



# def team_maker(start=1, cnt=0):
#     if cnt == N // 2:
#         global min_score
#         score = [0] * 2
#         for i in range(N - 1):
#             for j in range(i + 1, N):
#                 if team[i] == team[j]:
#                     score[team[i]] += nums[i][j] + nums[j][i]
#         if min_score > abs(score[0] - score[1]):
#             min_score = abs(score[0] - score[1])
#         return
#
#     for i in range(start, N):
#         if team[i] == 0:
#             team[i] = 1
#             team_maker(i + 1, cnt + 1)
#             team[i] = 0
#
#
# for case in range(int(input())):
#     N = int(input())
#     nums = [list(map(int, input().split())) for _ in range(N)]
#
#     team = [0] * N
#     min_score = 20000 * N
#     team_maker()
#
#     print("#{} {}".format(case + 1, min_score))
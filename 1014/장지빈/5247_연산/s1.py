import sys
sys.stdin = open('input.txt')
from collections import deque

def calc(cal, i):
    if not i:
        return cal + 1
    elif i == 1:
        return cal - 1
    elif i == 2:
        return cal * 2
    else:
        return cal - 10

def bfs(cal, cnt):
    global ans, target, used
    q = deque()
    q.append([cal, cnt])
    while q:
        newone = q.popleft()
        if newone[1] > ans:
            return
        if newone[0] == target:
            ans = newone[1]
            return
        for i in range(4):
            if not i:
                if 0 < calc(newone[0], i) < 1000001 and not used[calc(newone[0], i)]:
                    q.append([calc(newone[0], i), newone[1]+1])
                    used[calc(newone[0], i)] = 1
            elif i == 1:
                if 0 < calc(newone[0], i) < 1000001 and not used[calc(newone[0], i)]:
                    q.append([calc(newone[0], i), newone[1]+1])
                    used[calc(newone[0], i)] = 1
            elif i == 2:
                if 0 < calc(newone[0], i) < 1000001 and not used[calc(newone[0], i)]:
                    q.append([calc(newone[0], i), newone[1]+1])
                    used[calc(newone[0], i)] = 1
            else:
                if 0 < calc(newone[0], i) < 1000001 and not used[calc(newone[0], i)]:
                    q.append([calc(newone[0], i), newone[1]+1])
                    used[calc(newone[0], i)] = 1

# def bfs(cal, cnt):
#     global ans, used
#     q = []
#     q.append([cal, cnt])
#     while q:
#         newone = q.pop(0)
#         if newone[0] == target:
#             ans = cnt
#             break
#         for i in range(4):
#             a = calc(newone[0], i)
#             if a < 1000000 and not used[a]:
#                 q.append([a, cnt+1])
#                 used[a] = a

# def bfs(cal, cnt):
#     global ans, used
#     q = []
#     q.append([cal, cnt])
#     while q:
#         newcal = q.pop(0)
#         for i in range(4):
#             newone = calc(newcal[0], i)
#             if newone == target:
#                 if ans > cnt:
#                     ans = cnt
#             else:
#                 if 0 < newone < 1000000 and cnt < ans and newone != used[newone]:
#                     q.append([newone, newcal[1]+1])
#                     used[newone] = newone
#         return
#     return

# def dfs(cal, cnt):
#     global ans, calnum
#     if cnt > ans:
#         return
#     if cal > 1000000:
#         return
#     if cal == target:
#         if ans > cnt:
#             ans = cnt
#     dfs(cal+calnum[0], cnt+1)
#     dfs(cal+calnum[1], cnt+1)
#     dfs(cal*calnum[2], cnt+1)
#     dfs(cal+calnum[3], cnt+1)
#     return

for tc in range(1, int(input())+1):
    ans = 987654321
    n, target = map(int, input().split())
    calnum = [1, -1, 2, -10]
    used = [0] * 1000001
    bfs(n, 0)

    print('#{} {}'.format(tc, ans))
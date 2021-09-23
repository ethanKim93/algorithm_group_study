import sys
sys.stdin = open("input.txt")

N = int(input())
nums = list(map(int, input().split()))
left = [0] * (N+1)
right = [0] * (N+1)
adjlist = [[0,0] for _ in range(N+1)]

for i in range(len(nums)//2):
    n1, n2 = nums[i * 2], nums[i * 2 + 1]
    if adjlist[n1][0]:
        adjlist[n1][1] = n2
    else:
        adjlist[n1][0] = n2


def pre_order(n):   # 전위 순회
    if n:
        print(n)
        pre_order(adjlist[n][0])
        pre_order(adjlist[n][1])

pre_order(1)
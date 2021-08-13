import sys
sys.stdin = open('input.txt')

t = int(input())
for _ in range(1, t+1):
    tc, nums = input().split()
    nums = int(nums)
    maps = list(input().split())
    diffnum = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for i in range(nums-1, -1, -1):
        for x in range(i):
            if diffnum.index(maps[x]) > diffnum.index(maps[x+1]):
                 maps[x], maps[x+1] = maps[x+1], maps[x]

    print(tc)
    print(*maps)


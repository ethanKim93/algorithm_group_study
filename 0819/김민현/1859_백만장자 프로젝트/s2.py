import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N = int(input())
    nums = list(map(int,input().split()))
    i = 0
    total = 0
    max_idx = []

    for i in range(1,N):
        if nums[N-1] < nums[i]:
            max_idx.append(i)
    max_idx.append(N-1)

    k = 0
    for j in max_idx:
        a =0
        c =1
        for m in range(k,j):
           if nums[j]-nums[m] > 0:
               total = nums[j]-nums[m]
        k = j


    print('#{} {}'.format(tc,total))
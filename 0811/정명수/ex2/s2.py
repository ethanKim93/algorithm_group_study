import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    li = list(map(int,input().split()))
    n = len(li)
    arr=[]
    flag = 0
    for i in range(1<<n):
        s=[]
        for j in range(n):
            if i & (1<<j):
                s.append(li[j])
        arr.append(s)
    for k in arr:
        if sum(k)==0:
            flag += 1
    print(flag)


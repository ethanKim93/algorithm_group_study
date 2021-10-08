import sys
sys.stdin = open('sample_input.txt')

def find(s,e,target):
    global ans,left,right
    m = (s + e) // 2
    if target == num[m]:
        ans += 1
        return
    if e < s:
        return
    elif num[m]>target and left != 1:
        left = 1
        right = 0
        find(s,m-1,target)
    elif num[m]<target and right != 1:
        right = 1
        left = 0
        find(m+1,e,target)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    num = sorted(list(map(int,input().split())))
    in_num = list(map(int, input().split()))
    ans = 0
    for i in in_num:
        left = 0
        right = 0
        find(0,N-1,i)
    print('#{} {}'.format(tc,ans))
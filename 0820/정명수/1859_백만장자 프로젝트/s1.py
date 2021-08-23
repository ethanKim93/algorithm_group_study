import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    li = list(map(int,input().split()))
    stack=[len(li)-1]
    max_li = li[-1]
    for i in range(len(li)-2,-1,-1):
        if li[i] > max_li:
            max_li = li[i]
            stack.append(i)
    answer = 0
    stack = stack[::-1]
    temp = 0
    for j in stack:
        for i in range(temp,j):
            answer += (li[j]-li[i])
        temp = j+1
    print('#{} {}'.format(tc,answer))
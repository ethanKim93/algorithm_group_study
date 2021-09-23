import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    E, N = map(int, input().split())
    num = list(map(int,input().split()))
    left = [0]*(E+2)
    right = [0 for _ in range(E + 2)]
    for i in range(E):
        s,e = num[2*i],num[2*i+1]
        if left[s]:
            right[s] = e
        else:
            left[s] = e
    q = [N]
    cnt = 0
    while q:
        cnt += 1
        t = q.pop()
        if right[t]:
            q.append(right[t])
        if left[t]:
            q.append(left[t])
    print('#{} {}'.format(tc,cnt))


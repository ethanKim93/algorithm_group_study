#4408. 자기 방으로 돌아가기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    corr =[0]*201
    for _ in range(N):
        now, back = map(int, input().split())
        if now > back:
            now, back = back, now
        for i in range((now+1)//2, (back+1)//2+1):
            corr[i] += 1

    mt = 0
    for c in corr:
        if c >= mt:
            mt = c

    print('#{} {}'.format(tc, mt))
# #1244. [S/W 문제해결 응용] 2일차 - 최대 상금
T = int(input())
for tc in range(1, T+1):
    n, c = input().split()
    n = list(n)
    stn = sorted(n, reverse=True)
    res = ''

    cnt = int(c)
    idx = 0
    while cnt > 0:
        maxI = idx
        lct = 0
        if n == stn:
            break
        for j in range(idx+1, len(n)):
            if n[j:len(n)].count(max(n[j:len(n)])) > 1: # 바꿀 범위 내에 바꿀 가장 큰 수가 중복일 때
                for k in n[j:j+cnt]: # 앞으로 바꿀 범위 내에 바꿀 값보다 작은 값이 있으면
                    if k < n[idx]:
                        lct += 1 # 작은것들의 개수를 셈
            else:
                if n[maxI] <= n[j]:
                    maxI = j-lct
        if maxI != idx:
            n[maxI], n[idx] = n[idx], n[maxI]
            cnt -= 1
        idx += 1

    def check(n):
        global cnt
        if cnt:
            for i in n:
                if n.count(i) > 1:
                    cnt = 0
                    return
    check(n)
    def last_check(n):
        global cnt
        if cnt:
            if cnt%2:
                n[-1], n[-2] = n[-2], n[-1]
                cnt = 0
            else:
                cnt = 0
    last_check(n)
    print('#{} {}'.format(tc, res.join(n)))
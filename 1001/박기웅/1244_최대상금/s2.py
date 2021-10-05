def trade(i, t):
    global maxp, maxp_ex

    # 목표값이랑 안맞는 인덱스까지 인덱스 이동
    for j in range(n):
        if N[j] != goal[j]: 
            break
    i = j

    # 이미 목표값에 도달했거나 교환횟수가 끝날 시 
    if i == n-1 or t == T:
        if (T-t)%2 and not flag:    # 남은 교환 횟수가 홀수이고, 2개 이상의 중복 수가 없을시에
            N[-1], N[-2] = N[-2], N[-1]
            maxp_ex = int(''.join(map(str, N)))
            return 

        p =  int(''.join(map(str, N)))
        if p > maxp:
            maxp = p
        return
    else:
        for k in range(i, n):
            if k != i:
                N[k], N[i] = N[i], N[k]
                trade(i+1, t+1)
                N[k], N[i] = N[i], N[k]
            
for tc in range(1, int(input())+1):
    N, T = input().split()
    N, T = list(map(int, N)), int(T)
    n = len(N)
    goal = sorted(N, reverse=True)

    # 숫자 카운트 배열
    # 같은 숫자가 2개 이상인 경우 flag = 1
    flag = 0
    cnt = [0]*10
    for i in range(n):
        cnt[N[i]] += 1
        if cnt[N[i]] > 1:
            flag = 1

    maxp = maxp_ex = 0
    trade(0,0)
    if maxp_ex:
        maxp = maxp_ex
    print('#{} {}'.format(tc, maxp))
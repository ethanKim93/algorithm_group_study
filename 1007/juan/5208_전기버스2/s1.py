T = int(input())

def backtrack(now):
    global cnt
    stop, charge = now, BS[now]             # 현재 위치, 최대 이동 가능 거리
    cnt += 1                                # 배터리 교체 회수 + 1
    for i in range(now, now+BS[now]+1):     # 현재 위치부터 최대 이동 가능 거리 범위에서 순회
        if i + BS[i] > charge:              # 이동한 위치(i)에서 더 이동할 수 있는 거리를 더한 값과 기존 위치에서의 최대 이동 가능 거리 비교
            stop, charge = i, i + BS[i]     # 현재 위치, 최대 이동 가능 거리 갱신
        if charge >= N-1:                   # 갱신한 최대 이동 가능 거리가 목적지에 도달하면 종료
            return
    else:
        backtrack(stop)                     # 순회 후에는 최대 이동 가능한 위치 기준으로 다시 backtrack 함수 호출

for tc in range(1, T+1):
    bus = list(map(int, input().split()))
    N, BS = bus[0], bus[1:]
    cnt = now = 0
    backtrack(now)
    print('#{} {}'.format(tc, cnt))
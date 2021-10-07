import sys
sys.stdin = open('sample_input.txt')

def drive(bus_stop, destination, cnt):
    global charge
    route = []
    route.append(bus_stop)


    if cnt > charge:    # 중간에 이미 최소 횟수를 초과하면 가지치기
        return

    now = route.pop(0)                  # 현재 위치 now
    for i in range(1, can_go[now]+1):   # 현재 위치에서 갈 수 있는 정류장 다 넣어주기
        if now + i <= destination:
            route.append(now+i)

    while route:                        # 갈 수 있는 정류장
        go = route.pop(0)
        if go == destination:           # 만약 가려는 정류장이 목적지이면 return
            charge = cnt
            return
        drive(go, destination, cnt + 1)



T = int(input())
for tc in range(1, T+1):
    N_lst = list(map(int, input().split()))
    N = N_lst[0]
    can_go = [0]+N_lst[1:]      # index 사용 위해 [0] 추가해줌
    charge = N                  # 충전 할 수 있는 최대 횟수를 초기값으로 지정 -> 최소로 계속 바꿔줄 것임!
    drive(1, N, 0)
    print('#{} {}'.format(tc, charge))
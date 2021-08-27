def sale_slot(slot):
    if len(sale) <= slot:
        for idx_2 in range(len(sale), slot):
            sale.append(0)
        sale.append(1)
    else:
        sale[slot] += 1
    return

def take_out_cnt(slot):
    result = 0
    for idx_3 in range(slot + 1):
        result += sale[idx_3]
    return result

T = int(input())
for tc in range(1, 1 + T):
    N, M, K = map(int, input().split())  # 인원, 생산 시간, 생산량
    enter = list(map(int, input().split()))  # 도착 시간
    sale = [0]  # 시간대 별 판매량
    result = 'Possible'

    for idx_1 in range(N):
        # 만들기도 전에 오면 웨이팅
        if enter[idx_1] < M:
            result = 'Impossible'
            break

        sale_slot(enter[idx_1] // M) # 손님이 온 시간대
        take_out = take_out_cnt(enter[idx_1] // M) # 손님이 도착했을 때 지금까지 가져간 양
        amount = (enter[idx_1] // M) * K - take_out # 만들어 놓은 양 - 가져간 양

        # 만들어 놓은 양보다 가져간 양이 많으면 웨이팅
        if amount < 0:
            result = 'Impossible'
            break

    print("#{} {}".format(tc, result))

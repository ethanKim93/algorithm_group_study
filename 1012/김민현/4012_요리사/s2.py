#온라인 퍼옴

def comb(cnt, idx, start):  # 조합 찾기
    # 현재 선택한 개수, p1의 값을 바꿔 줄 위치 값, 시작점

    if cnt == find_num:  # 현재 선택한 개수가 찾으려는 숫자와 같은 경우
        cal(0)
        return

    else:
        for q in range(start, n):
            p1[idx] = q
            comb(cnt + 1, idx + 1, q + 1)  # 선택한 개수 + 1, 위치 + 1, 시작점은 현재 값 + 1
    return


def cal(p2_cnt):  # 계산
    global min_res
    customer1 = 0  # 고객 1의 합
    customer2 = 0  # 고객 2의 합

    for w in range(n):  # 고객 2의 재료 선택
        if w not in p1:
            p2[p2_cnt] = w
            p2_cnt += 1

    for i in range(n // 2):  # 계산하기, 홀수가 존재하기 때문에 하나씩 뽑아서 대조하면서 계산
        # if n == 6이면 n//2 == 3이고, 두개씩 짝 지으면 한 개가 남아버림

        for j in range(n // 2):
            if i != j:  # 같은 값 제외 [1, 2]에서 1+1 같은 경우 배제하기 위함
                customer1 += foods[p1[i]][p1[j]]
                customer2 += foods[p2[i]][p2[j]]

    if abs(customer1 - customer2) < min_res:  # min_res보다 작으면 값 바꾸기
        min_res = abs(customer1 - customer2)

    return


T = int(input())

for tc in range(1, 1 + T):
    n = int(input())

    foods = [list(map(int, input().split())) for _ in range(n)]  # 시너지 표

    min_res = 20000 * n  # 최소 값, 시너지 최대 값 * n

    p1 = [0] * (n // 2)  # 1번 고객의 재료를 저장하기 위함
    p2 = [0] * (n // 2)  # 2번 고객의 재료를 저장하기 위함

    find_num = n // 2  # 선택해야 할 개수

    comb(0, 0, 0)  # 현재 선택한 개수, p1의 값을 바꿔 줄 위치 값, 시작점

    print('#{} {}'.format(tc, min_res))
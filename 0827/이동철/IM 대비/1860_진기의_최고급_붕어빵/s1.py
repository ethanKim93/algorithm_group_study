import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # N의 사람
    # M초의 시간 동안 K개의 붕어빵
    N, M, K = map(int, input().split())
    customers = sorted(list(map(int, input().split())))
    result = 'Possible'

    # timeline : customer => // M * K
    # 해당시간 만들 수 있는 빵의 최대 갯수
    # 팔린 빵의 갯수
    sold_bread = 0
    for customer in customers:
        # 손님이 도착한 시간에 최대로 만들 수 있는 빵의 갯수
        made_bread = (customer // M) * K

        # 남은 빵의 갯수
        remain = made_bread - sold_bread

        if remain <= 0:
            result = 'Impossible'
            break
        else:
            sold_bread += 1

    print('#{} {}'.format(tc, result))


# T = int(input())
# for tc in range(1, T + 1):
#     N, M, K = map(int, input().split())
#     # N: 사람수, M초의 시간을 들이면 K개의 붕어 만들 수 있음
#     N_list = list(map(int, input().split()))
#     # N명의 사람이 각각 언제 도착하는지를 초 단위
#
#     for i in range(N):
#         if sorted(N_list)[i] // M * K < i + 1:
#             # N_list[i]초 일때의 붕어생산량과 그 전에 사간 사람의 수를 빼면
#             # N_list[i]초의 붕어빵 재고를 알 수 있다.
#             # N_list[i]초까지 만들어진 붕어 개수: (N_list[i] // M) * K
#             # 왜냐하면 단위 시간(M)으로 나눈 몫만큼 만들 수 있고,
#             # 그때마다 K개를 만들기 때문이다.
#             # 인당 1개씩 구매하기 때문에 (N_list[i] // M) * K 에서 인덱스+1 만큼 빼주면 된다.
#             result = 'Impossible'
#             break
#         else:
#             result = 'Possible'
#
#     print('#{} {}'.format(tc, result))
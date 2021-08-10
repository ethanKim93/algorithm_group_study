import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))




    total_list = []
    i = 0


    # 합 구하기
    while len(num_list) >= M:
        total = 0
        for i in range(M):
            total += num_list[i]
        total_list.append(total)
        num_list = num_list[1:]


    # 차이
    for a in range(len(total_list)-1, 0, -1):
        for i in range(0, a):
            if total_list[i] > total_list[i+1]:
                total_list[i], total_list[i+1] = total_list[i+1], total_list[i]



    interval = total_list[-1] - total_list[0]

    print('#{} {}'.format(tc, interval))







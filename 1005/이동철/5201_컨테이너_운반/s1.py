import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N은 컨테이너 수, M은 트럭 수

    N_weight = sorted(list(map(int, input().split())), reverse=True)
    # N개의 화물의 무게
    M_weight = sorted(list(map(int, input().split())), reverse=True)
    # M개 트럭의 적재용량
    # 무거운 것 부터 고려하기 위해 sorted reverse

    result = 0
    cnt = 0
    truck, container = 0, 0
    while True:
        if cnt == min(N, M):
            # N과 M의 최소 크기보다 작을 때만 반복
            break
        if M_weight[truck] >= N_weight[container]:
            result += N_weight[container]
            # 화물의 용량이 트럭의 적재용량보다 작으면 결과값에 더한다
            truck += 1
            container += 1
        else:
            container += 1
        cnt += 1

    print('#{} {}'.format(tc, result))

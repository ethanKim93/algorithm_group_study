import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    truck_num, container_num = map(int, input().split())
    container_weight = sorted(list(map(int, input().split())))  # 컨테이너 무게 정렬
    truck_weight = sorted(list(map(int, input().split())))      # 트럭 적재량 정렬



    total = 0
    while truck_weight:                             # 트럭이 다 떠날때 까지 반복
        t = truck_weight.pop()                      # 현재 트럭 중 적재량이 가장 큰 트럭
        while container_weight:                     # 컨테이너를 다 실을때 까지 반복
            c = container_weight.pop()              # 현재 컨테이너 중 무게가 가장 큰 컨테이너
            if t >= c:                              # 트럭에 실을 수 있으면 total에 더함
                total += c
                break                               # 트럭에 컨테이너를 실으면 다음 트럭으로 넘어감

    print('#{} {}'.format(tc, total))
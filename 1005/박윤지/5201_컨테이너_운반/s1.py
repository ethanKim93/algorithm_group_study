# 처음 생각난대로 푼건데... 이게 greedy 탐색법인지도 모르겠다.
# 왜 맞는지도 잘 모르겠음.

# # 람다 함수 사용 정렬
# sorted_time = sorted(sche, key=lambda x: x[1])

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))  # 화물의 무게
    truck = list(map(int, input().split()))  # 트럭의 용량
    # 리스트 정렬 없이 트럭 용량 앞에서부터 순회하면서
    # 용량보다 작거나 같은 것중 가장 큰 것 선택해서 더하기
    ans = 0
    for i in truck:
        maxV = 0
        for j in container:
            if i >= j and maxV < j:
                maxV = j
        if maxV == 0:
            # pass
            continue  # pass보다는 여기서 바로 조건으로 돌리는 게 좋다
        else:
            ans += maxV
            container.remove(maxV)
    print('#{} {}'.format(tc, ans))


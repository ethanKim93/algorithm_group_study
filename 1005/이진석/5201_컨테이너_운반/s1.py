import sys
sys.stdin = open('')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    total = 0
    # 내림차순 정렬(Bubble Sort)
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if containers[i] > containers[j]:
                containers[i], containers[j] = containers[j], containers[i]

    for i in range(M - 1, 0, -1):
        for j in range(i):
            if trucks[i] > trucks[j]:
                trucks[i], trucks[j] = trucks[j], trucks[i]


    i = j = 0
    while i < len(trucks):
        if j <= len(containers)-1 and trucks[i] >= containers[j]:   # 유효한 인덱스(container)면서 트럭에 적재 가능한 무게일때
            total += containers.pop(j)                              # 컨테이너를 pop해서 합에 추가
            i += 1                                                  # 인덱스 갱신(다음트럭, 첫번째 컨테이너)
            j = 0
        else:                                                       # 인덱스가 유효하지 않거나 트럭에 적재불가능한 무게일때
            if j < len(containers) - 1:                             # j 인덱스 유효하면
                j += 1                                              # j 1 증가
            else:                                                   # 유효하지 않다면
                i += 1                                              # 다음트럭, 첫번째 컨테이너
                j = 0

    print('#{} {}'.format(tc, total))
# 대표 코드(김주호)
for case in range(int(input())):
    # N 컨테이너 개수 M 트럭 수
    N, M = map(int, input().split())
    # 화물은 하나씩만 담을 수 있으므로 가장 큰 화물을 가장 큰 트럭에 담기위해
    # 큰 순서대로 정렬
    freights = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)

    # 옮겨진 화물 전체 무게를 담아줄 total
    total = 0
    # 트럭의 인덱스
    truck_idx = 0
    # 화물의 인덱스
    freight_idx = 0

    # 범위까지 while문 돌기
    while freight_idx < N and truck_idx < M:
        # 트럭 용량이 컨테이너 무게보다 작거나 같은 경우에만 화물을 싣을 수 있으므로
        if trucks[truck_idx] >= freights[freight_idx]:
            # 그때만 total에 화물 무게 더해주기
            total += freights[freight_idx]
            # 그리고 트럭 인덱스 하나 up
            truck_idx += 1
        # if문 끝나면 화물 인덱스 하나 up
        freight_idx += 1

    print("#{} {}".format(case + 1, total))
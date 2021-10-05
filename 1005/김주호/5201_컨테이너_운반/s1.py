for case in range(int(input())):
    N, M = map(int, input().split())
    freights = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)

    total = 0
    truck_idx = 0
    freight_idx = 0
    while freight_idx < N and truck_idx < M:
        if trucks[truck_idx] >= freights[freight_idx]:
            total += freights[freight_idx]
            truck_idx += 1
        freight_idx += 1

    print("#{} {}".format(case + 1, total))

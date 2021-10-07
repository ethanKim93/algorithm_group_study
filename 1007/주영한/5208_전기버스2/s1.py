for tc in range(1, int(input()) + 1):
    charge = list(map(int, input().split()))
    destination = charge[0] - 1
    charge = charge[1:]
    result = -1
    idx = 0
    while idx < destination:
        max_pos = idx
        max_idx = idx
        for i in range(1, charge[idx] + 1):
            move = idx + i
            if move >= destination:
                idx = move
                break

            if max_pos < move + charge[move]:
                max_pos = move + charge[move]
                max_idx = i
        idx += max_idx
        result += 1

    print("#{} {}".format(tc, result))
def half(start, end):
    if end - start <= 1:
        return
    else:
        H = start + end
        half(start, H // 2)
        half(H // 2, end)

        left = nums[start: H // 2]
        L_idx = 0
        right = nums[H // 2: end]
        R_idx = 0

        global total
        if left[-1] > right[-1]:
            total += 1

        put = start
        while put < end:
            if R_idx >= len(right) or (L_idx < len(left) and left[L_idx] < right[R_idx]):
                nums[put] = left[L_idx]
                L_idx += 1
            elif L_idx >= len(left) or (R_idx < len(right) and left[L_idx] >= right[R_idx]):
                nums[put] = right[R_idx]
                R_idx += 1
            put += 1


for case in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    total = 0
    half(0, N)
    print("#{} {} {}".format(case + 1, nums[N//2], total))

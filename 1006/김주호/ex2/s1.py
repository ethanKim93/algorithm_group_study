def powerset(start=0, total=0):
    if total > 10:
        return

    if total == 10:
        for i in range(10):
            if not check[i]:
                print(nums[i], end=" ")
        print()
        return

    for i in range(start, 10):
        if check[i]:
            check[i] = False
            powerset(i + 1, total + nums[i])
            check[i] = True


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check = [True] * 10
powerset()

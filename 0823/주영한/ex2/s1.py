def backtracking(base_list, sub_sum, target, start_idx, N):
    if sub_sum >= target:
        if sub_sum == target:
            print(base_list)
        return

    for idx in range(start_idx, N):
        base_list.append(arr[idx])
        sub_sum += arr[idx]
        backtracking(base_list, sub_sum, target, idx + 1, N)
        base_list.pop()
        sub_sum -= arr[idx]
    return

arr = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
backtracking([], 0, 10, 0, 10)
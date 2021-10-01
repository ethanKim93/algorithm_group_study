def sel_sort(next_idx):
    min_idx = next_idx
    if next_idx != len(nums) - 1:
        for idx in range(next_idx, len(nums)):
            if nums[min_idx] > nums[idx]:
                min_idx = idx
        nums[next_idx], nums[min_idx] = nums[min_idx], nums[next_idx]
        sel_sort(next_idx+1)

    return


nums = [88, 12, 46, 48, 32, 65, 48, 1, 989, 23, 4, 89]
sel_sort(0)
print(nums)
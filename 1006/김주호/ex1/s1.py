def quick_sort(start, end):
    if -1 <= start - end:
        return

    pivot = nums[start]
    bigger = start + 1
    smaller = end - 1

    while True:
        while bigger < end - 1 and pivot >= nums[bigger]:
            bigger += 1
        while start < smaller and pivot <= nums[smaller]:
            smaller -= 1

        if bigger >= smaller:
            nums[start], nums[smaller] = nums[smaller], nums[start]
            quick_sort(start, smaller)
            quick_sort(bigger, end)
            return
        else:
            nums[bigger], nums[smaller] = nums[smaller], nums[bigger]


nums = list(map(int, input().split()))
quick_sort(0, len(nums))
print(nums)

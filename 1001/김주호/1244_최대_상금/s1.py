import sys
sys.stdin = open("input.txt")

for case in range(int(input())):
    data = input().split()
    N = int(data[1])
    nums = list(map(int, data[0]))

    nums_sort = sorted(nums, reverse=True)

    if N < len(nums) // 2 and nums_sort != nums:
        pick_min = []
        pick_max = [[] for _ in range(10)]
        for i in range(0, N):
            if nums[i] != nums_sort[i]:
                pick_min.append(i)
                for j in range(len(nums) - 1, -1, -1):
                    if nums[j] == nums_sort[i] and j not in pick_max[nums_sort[i]]:
                        pick_max[nums_sort[i]].append(j)
                        break

        L = len(pick_min)

        for idx in range(L):
            nums[pick_min[idx]], nums[pick_max[nums_sort[idx]][-1]] = nums[pick_max[nums_sort[idx]][-1]], nums[
                pick_min[idx]]
            del (pick_max[nums_sort[idx]][-1])

    else:
        N -= len(nums) // 2 if nums_sort != nums else 0

        flag = False

        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    flag = True
                    break
            if flag:
                break

        if N % 2 and not flag:
            nums_sort[-1], nums_sort[-2] = nums_sort[-2], nums_sort[-1]
        nums = nums_sort

    print("#{} ".format(case + 1), end="")
    for num in nums:
        print("{}".format(num), end="")
    print()
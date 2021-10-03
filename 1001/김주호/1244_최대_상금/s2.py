import sys
sys.stdin = open("input.txt")

for case in range(int(input())):
    data = input().split()
    N = int(data[1])
    nums = list(map(int, data[0]))
    nums_sort = sorted(nums, reverse=True)

    check = [[] for _ in range(10)]
    L = len(nums)
    while N and nums != nums_sort:
        flag = False
        for front in range(L):
            if nums[front] != nums_sort[front]:
                for back in range(L - 1, -1, -1):
                    if nums[back] == nums_sort[front]:
                        nums[front], nums[back] = nums[back], nums[front]
                        check[nums[front]].append(back)

                        if len(check[nums[front]]) > 1:
                            li = []
                            for idx in check[nums[front]]:
                                li.append(nums[idx])
                            li.sort()
                            for idx in check[nums[front]]:
                                nums[idx] = li.pop(0)

                        flag = True
                        break
                if flag:
                    break
        N -= 1

    if N % 2:
        if len(set(nums)) == len(nums):
            nums[-1], nums[-2] = nums[-2], nums[-1]

    print("#{}".format(case + 1), end=" ")
    print(*nums, sep="")

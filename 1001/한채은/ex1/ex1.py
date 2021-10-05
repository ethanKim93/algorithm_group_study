nums = [88, 12, 46, 48, 32, 65, 48, 1, 989, 23, 4, 89]

def recursion(llist):
    if llist != []:
        x = min(llist)
        arr = [x]
        llist.remove(x)
        return arr + recursion(llist)
    else:
        return []


print(recursion(nums))

# 주호님 코드
# def sort(start=0):
#     if start == N:
#         return
#
#     min_idx = start
#     for i in range(start + 1, N):
#         if nums[min_idx] > nums[i]:
#             min_idx = i
#     nums[start], nums[min_idx] = nums[min_idx], nums[start]
#     sort(start+1)
#
#
# nums = [88, 12, 46, 48, 32, 65, 48, 1, 989, 23, 4, 89]
# N = len(nums)
#
# sort()
#
# print(nums)
def powerset(idx, sub_num):
    if idx == 10:
        p_sum = 0
        p_list = []
        for index, i in enumerate(sel):
            if i:
                p_sum += arr[index]
                p_list.append(arr[index])
        if p_sum == sub_num:
            print(*p_list)
        return
    sel[idx] = 1
    powerset(idx+1, sub_num)
    sel[idx] = 0
    powerset(idx+1, sub_num)


arr = list(range(1, 11))
sel = [0] * 10
powerset(0, 10)

# 비트 연산자
# result = []
# for i in range(1<<10):
#     p_list = []
#     p_sum = 0
#     for j in range(10):
#         if i & (1<<j):
#             p_sum += arr[j]
#             p_list.append(arr[j])
#     if p_sum == 10:
#         result.append(p_list)
# print(result)


# arr = [1, 2, 3]
# N = len(arr)
# sel = [0] * N       # [0, 0, 0]
#
#
# def powerset(idx):
#     if idx == N:
#         for index, i in enumerate(sel):
#             if i:
#                 print(arr[index], end=' ')
#         print()
#         return
#     sel[idx] = 1        # 1번 [1, 0, 0]         # 2번 [1, 1, 0]         # 3번 [1, 1, 1]         # 6번 [1, 0, 1]
#     powerset(idx+1)     # powerset(1)           # powerset(2)           # powerset(3)           # powerset(3)
#     sel[idx] = 0        # 4번 [1, 1, 0]         # 5번 [1, 0, 0]         # 7번 [1, 0, 0]
#     powerset(idx+1)     # powerset(3)           # powerset(2)           # powerset(3)
#
#
# powerset(0)


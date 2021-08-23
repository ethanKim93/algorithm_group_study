arr = [1, 2, 3]

def ps(i, N):
    if i == N:
        print(arr)
    else:
        for j in range(1, N):
            arr[i], arr[j] = arr[j], arr[i]
            ps(i+1, N)
            arr[i], arr[j] = arr[j], arr[i]

ps(0, len(arr))

# arr = [_ for _ in range(1, 11)]
# N = len(arr)
# sel = [0] * N
#
# def powerset(idx, sum_num):
#     if sum_num > 10:
#         return
#     if idx == N:
#         if sum_num == 10:
#             for i in range(idx):
#                 if sel[i]:
#                     print(arr[i], end=" ")
#             print()
#         return
#     else:
#         sel[idx] = 1
#         powerset(idx+1, sum_num+arr[idx])
#         sel[idx] = 0
#         powerset(idx+1, sum_num)
#
# powerset(0,0)
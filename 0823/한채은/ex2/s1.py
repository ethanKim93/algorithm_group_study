# # solve 1
# arr = [1, 2, 3]
# n = len(arr)
#
# for i in range(1 << n):
#     for j in range(n):
#         if i & (1 << j):
#             print(arr[j], end='')
#     print()
#
# # solve 2
# def f(k, n):
#     if n == k:
#         for i in range(n):
#             if b[i] == 1:
#                 print(arr[i], end='')
#         print()
#     else:
#         b[k] = 0
#         f(k+1, n)
#         b[k] = 1
#         f(k+1, n)
#
# arr = [1, 2, 3]
# b = [0, 0, 0]
# f(0, 3)

# solve 3
arr = [i for i in range(1, 11)]
N = len(arr)
sel = [0] * N

def powerset(idx, sub_sum):
    if idx == N:
        if sub_sum == 10:
            for index, i in enumerate(sel):
                if i == 1:
                    print(arr[index], end=" ")
            print()
        return
    sel[idx] = 1
    powerset(idx+1, sub_sum+arr[idx])
    sel[idx] = 0
    powerset(idx+1, sub_sum)

powerset(0, 0)
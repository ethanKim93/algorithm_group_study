# def select(arr):
#     for i in range(len(arr) - 1):
#         idx = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[idx]:
#                 idx = j
#         arr[i], arr[idx] = arr[idx], arr[i]
#     return arr
#
#
# print(select([1,442,1231254,123124,32423,23423,123,5435]))
# 그냥 선택정렬 구현
lis = [1, 32, 44, 65, 23, 13, 4, 55, 65, 56]

def selection_sort(lis, s, e):
    idx = s

    if s == e:
        return

    for j in range(s+1, e, 1):
        if lis[j] < lis[idx]:
            idx = j

    lis[s], lis[idx] = lis[idx], lis[s]
    selection_sort(lis, s + 1, e)

selection_sort(lis, 0, 10)
print(lis)
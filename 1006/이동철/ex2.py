# 모든 부분 집합 구하기
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# cnt = 0
#
# def powerset(array):
#     global cnt
#     # a list containing an empty tuple
#     arr_list = [()]
#     for num in array:
#         for i in range(len(arr_list)):
#             curr_subset = arr_list[i]
#             # append one more number to the tuple
#             curr_subset += (num,)
#             arr_list.append(curr_subset)
#             cnt += 1
#     return arr_list
#
#
# print(powerset(arr))
# print(cnt)


# arr = list(map(int, input().split()))
#
# visited = [0] * len(arr)
# result = len(arr)
#
#
# def backtrack(s, total):
#     global visited, result, arr
#     if s > len(arr):
#         return
#     if total >= result:
#         if total == result:
#             for idx in range(len(arr)):
#                 if visited[idx]:
#                     print(arr[idx], end=' ')
#             print()
#         return
#
#     for i in range(s, len(arr)):
#         if not visited[i]:
#             visited[i] = 1
#             backtrack(i + 1, total + arr[i])
#             visited[i] = 0
#
#
# backtrack(0, 0)


# 명수님 풀이
A = list(map(int, input().split()))
limit = len(A)
visited = [0]*(limit+1)


def backtrack(arr, i, hap):
    if i > limit-1:
        return
    if hap > 10:
        return
    if hap == 10:
        for j in range(limit):
            if arr[j]:
                print(A[j],end=' ')
        print()
        return
    arr[i] = 1
    backtrack(arr, i+1, hap+A[i])
    arr[i] = 0
    backtrack(arr, i+1, hap)


backtrack(visited, 0, 0)

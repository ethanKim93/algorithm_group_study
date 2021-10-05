# 재귀 버전
def selectionSort(xs):
    if xs != []:
        smallest = min(xs)
        xs.remove(smallest)
        return [smallest] + selectionSort(xs)
    else:
        return []


xs = [3, 4, 1, 2, 56, 7, 78, 8]
print(selectionSort(xs))


# 재귀 버전
def s_sort(ls, N):
    if N == len(li):
        return ls
    else:
        min_n = N
        for i in range(N, len(li)):
            if li[i] < li[min_n]:
                min_n = i
        li[N], li[min_n] = li[min_n], li[N]
        return s_sort(ls, N+1)


li = [3, 4, 1, 2, 56, 7, 78, 8]
print(s_sort(li, 0))


# # 꼬리 재귀 버전
# def selectionSort(xs):
#     def loop(xs, ss):
#         if xs != []:
#             smallest = min(xs)
#             xs.remove(smallest)
#             return loop(xs, [smallest] + ss)  # ss.append(smallest) return loop(xs,ss)
#         else:
#             return ss
#
#     return loop(xs, [])
#
#
# # while 루프 버전
# def selectionSort(xs):
#     ss = []
#     while xs != []:
#         smallest = min(xs)
#         xs.remove(smallest)
#         ss = [smallest] + ss  # ss.append(smallest)
#     return ss

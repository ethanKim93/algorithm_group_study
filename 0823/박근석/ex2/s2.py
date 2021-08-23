# arr = [1,2,3]
# n = len(arr)
#
# for i in range(1<<n):
#     part = []
#     for j in range(len(arr)+1):
#         if i & (1<<j):
#             part.append(arr[j])
#     print(part)
#################################
arr = [1,2,3]
N = len(arr)
sel = [0] * N

def powerset(idx):
    if idx == N:
        for index, i in enumerate(sel):
            if i:
                print(arr[index], end=' ')
        print()
        return
    sel[idx] = 1
    powerset(idx+1)
    sel[idx] = 0
    powerset(idx+1)
powerset(0)
##################################
# def powerset(idx, subsum):
#     if idx == N:
#         total = 0
#         for index, i in enumerate(sel):
#             if i:
#                 print(arr[index], end=' ')
#         print()
#         return
#     sel[idx] = 1
#     powerset(idx+1)
#     sel[idx] = 0
#     powerset(idx+1)
# powerset(0)
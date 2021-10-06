from collections import deque
import sys
sys.stdin = open('sample_input.txt')

def mergeSort(A):
    N = len(A)
    if N == 1:
        return A
    L = A[0:N//2]
    R = A[N//2:N]
    L = mergeSort(L)
    R = mergeSort(R)
    
    global cnt
    L = deque(L)
    R = deque(R)
    result = deque()
    flag = 0
    while len(L) > 0 or len(R) > 0:
        if len(L) > 0 and len(R) > 0:
            if L[0] <= R[0]:
                result.append(L.popleft())
            else:
                result.append(R.popleft())
        elif len(L) > 0:
            result.append(L.popleft())
            flag = 1
        elif len(R) > 0:
            result.append(R.popleft())
    if flag: cnt += 1

    return result



# mergeSort와 merge 두 부분으로 나누어서 진행하면 swea에서 재귀함수 호출 한계에 도달해서 runtime error 발생함
# 이해하는 건 두 개의 함수로 나누는게 쉽지만 시간은 하나의 함수로 합치는 게 빠름

# def mergeSort(A):
#     N = len(A)
#     if N == 1:
#         return A
#     L = A[0:N//2]
#     R = A[N//2:N]
#     L = mergeSort(L)
#     R = mergeSort(R)
#     return merge(L, R)

# def merge(L, R):
#     global cnt
#     L = deque(L)
#     R = deque(R)
#     result = deque()
#     flag = 0
#     while len(L) > 0 or len(R) > 0:
#         if len(L) > 0 and len(R) > 0:
#             if L[0] <= R[0]:
#                 result.append(L.popleft())
#             else:
#                 result.append(R.popleft())
#         elif len(L) > 0:
#             result.append(L.popleft())
#             flag = 1
#         elif len(R) > 0:
#             result.append(R.popleft())
#     if flag: cnt += 1
    
#     return result



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    
    print('#{} {} {}'.format(tc, mergeSort(A)[len(A)//2], cnt))
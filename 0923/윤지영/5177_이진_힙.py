import sys
sys.stdin = open('input.txt')

def heap_add(n):
    if n <= N:
        heap[n] = li[n-1]
        while heap[n] < heap[n//2]:
            heap[n], heap[n//2] = heap[n//2], heap[n]
            n //=2
    else:
        return


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    li = list(map(int,input().split()))
    heap = [0] * (N+1)
    heap[1] = li[0]
    for p in range(1,N//2+1):
        c1, c2 = p*2, p*2+1
        heap_add(c1)
        heap_add(c2)
    result = 0
    k = N//2
    while k :
        result += heap[k]
        k = k//2

    print('#{} {}'.format(tc, result))



# 반복
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     li = list(map(int,input().split()))
#     heap = [0] * (N+1)
#     heap[1] = li[0]
#     for p in range(1,N//2+1):
#         c1, c2 = p*2, p*2+1
#         if c1 <= N:
#             heap[c1] = li[c1-1]
#             while heap[c1] < heap[c1//2]:
#                 heap[c1], heap[c1//2] = heap[c1//2], heap[c1]
#                 c1 //= 2            # 한번 바꾼다면, 바꾼 수랑 부모의부모와의 비교 필요!
#         else:
#             break
#         if c2 <= N:
#             heap[c2] = li[c2-1]
#             while heap[c2] < heap[c2//2]:
#                 heap[c2], heap[c2//2] = heap[c2//2], heap[c2]
#                 c2 //= 2
#         else:
#             break
#     result = 0
#     k = N//2
#     while k :
#         result += heap[k]
#         k = k//2

#     print('#{} {}'.format(tc, result))
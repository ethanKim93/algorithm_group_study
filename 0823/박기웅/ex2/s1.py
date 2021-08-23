# 비트 연산자 활용
# arr = [1, 2, 3]
# n = len(arr)
# def part(arr):
#     for i in range(1<<n):
#         part = []
#         for j in range(n):
#             if i & 1<<j:
#                 part.append(arr[j])
#         print(part)
#
# part(arr)

# 재귀로 부분집합 만들기
# arr = [1, 2, 3]
# N = len(arr)
# sel = [0]*N
#
# def powerset(idx):
#     if idx == N:
#         for index, i in enumerate(sel):
#             if i:
#                 print(arr[index], end=' ')
#         print()
#         return      # 재귀 중지
#     sel[idx] = 1    # 1. [1, 0, 0]      # 2. [1, 1, 0]   #3. [1, 1, 1]      # 6. [1, 0, 1]
#     powerset(idx+1) # powerset(1)       #powerset(2)    #powerset(3)        #powerset(3)
#     sel[idx] = 0    # 4. [1, 1, 0]      # 5. [1, 0, 0]  # 7. [1, 0, 0]
#     powerset(idx+1) # powerset(3)       #powerset(2)    #powerset(3)
#
# powerset(0)

arr = range(1, 11)
N = len(arr)
sel = [0]*N

def powerset(idx, subsum):
    if subsum == 10:
        for index, i in enumerate(sel):
            if i:
                print(arr[index], end=" ")
        print()
        return
    elif idx < N and subsum < 10:
        sel[idx] = 1
        powerset(idx + 1, subsum + arr[idx])
        sel[idx] = 0
        powerset(idx + 1, subsum)
    else:
        return

powerset(0, 0)
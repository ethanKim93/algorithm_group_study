
arr = [6, 6, 7, 7, 6, 7]

def babygin(numbers):
    temp = [0 for _ in range(10)]
    cnt = 0

    for number in numbers:
        temp[number] += 1

    idx = 0
    while idx < len(temp):
        if temp[idx] >= 3:
            temp[idx] -= 3
            cnt += 1
            continue

        if idx < len(temp) - 2:
            if temp[idx] and temp[idx+1] and temp[idx+2]:
                temp[idx] -= 1
                temp[idx+1] -= 1
                temp[idx+2] -= 1
                cnt += 1
                continue

        if cnt == 2:
            return 'Baby Gin!'
        idx += 1
    return 'Not Baby Gin!'


print(babygin(arr))


# #2. baby gin - 재귀
# """
# Baby gin Game Rule
#  0에서 9사이의 숫자 카드에서 임의로 카드 6장을 뽑을 때
#   - 3장의 카드가 연속적인 번호를 갖는 경우 run
#   - 3장의 카드가 동일한 번호를 갖는 경우 triplet
#
# 가능한 조합
# - run 2개
# - triplet 2개
# - run 1개 triplet 1개
# """
#
# # Baby Gin - permutation (recursion)
#
# # baby gin
# arr = [6, 6, 7, 7, 6, 7]
# # arr = [0, 5, 4, 0, 6, 0]
#
# # not baby gin
# # arr = [1, 2, 4, 7, 8, 3]
# # arr = [1, 0, 1, 1, 2, 3]
#
#
# def baby_gin():
#     global flag
#     check = 0
#
#     #1. 연속하는 3자리 수가 모두 같은 경우
#     if arr[0] == arr[1] and arr[1] == arr[2]: check += 1
#     if arr[3] == arr[4] and arr[4] == arr[5]: check += 1
#
#     #2. 연속하는 세 자리수
#     if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]: check += 1
#     if arr[3] + 1 == arr[4] and arr[4] + 1 == arr[5]: check += 1
#
#     #3. 2개 나오는 경우 baby gin
#     if check == 2:
#         flag = 1
#         return
#
#
# # 순열
# def perm(n, k):
#     if n == k:
#         baby_gin()
#     else:
#         for i in range(k, n-1, -1):
#             arr[k], arr[i] = arr[i], arr[k]   # 교환
#             perm(n+1, k)                      # 한 뎁스 이동
#             arr[k], arr[i] = arr[i], arr[k]   # 원상복구
#
#
# flag = 0
# perm(0, 5)  # idx 0 ~ 5
#
# if flag: print('Baby Gin!')
# else: print('Not Baby Gin!')
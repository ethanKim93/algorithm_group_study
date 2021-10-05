#
arr = [1, 2, 3, 4, 4, 4]

cnt = [0 for _ in range(12)]

def babygin(numbers):
    cnt = [0 for _ in range(10)]
    run = 0
    tri = 0

    for number in numbers:
        cnt[number] += 1

    idx = 0
    while idx < len(cnt):
        if cnt[idx] >= 3:
            cnt[idx] -= 3
            tri += 1
            continue

        if idx < len(cnt) - 2:
            if cnt[idx] and cnt[idx+1] and cnt[idx+2]:
                cnt[idx] -= 1
                cnt[idx + 1] -= 1
                cnt[idx + 2] -= 1
                run += 1
                continue

        if tri and run:
            return 'Baby Gin!'
        idx += 1
    return 'no'

print(babygin(arr))

# Baby Gin - permutation (recursion)

# baby gin
#arr = [6, 6, 7, 7, 6, 7]
#arr = [0, 5, 4, 0, 6, 0]

#not baby gin
arr = [1, 2, 4, 7, 8, 3]
#arr = [1, 0, 1, 1, 2, 3]


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
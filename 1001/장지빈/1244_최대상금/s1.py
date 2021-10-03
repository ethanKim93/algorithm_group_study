import sys
sys.stdin = open('input.txt')

def change(lst, N):
    n = len(lst)
    if N == 0:  # N 완성일 시 반환
        return lst
    if n <= 2:  # 최적으로 바꾼 후 남은 교환 숫자가 짝수/홀수인지를 판단. 짝수면 그대로 반환
        if N % 2 == 0:
            return lst
        elif N % 2:
            for ls in range(len(lst)-2):
                if lst[ls] == lst[ls+1]:        # 같은 숫자가 있어서 교환해도 최대값이 안바뀌면 그대로 반환
                    return lst
                                                 # 같은 숫자가 없다면 1,2값과 마지막 / 마지막-1값을 비교해서 반환
        try:
            if lst[0] - lst[1] >= lst[-1] - lst[-2]:
                lst[0], lst[1] = lst[1], lst[0]
                return lst
            else:
                lst[-1], lst[-2] = lst[-2], lst[-1]
                return lst
        except:
            lst[0], lst[1] = lst[1], lst[0]
            return lst

    temp = []
    Ma = 0
    for i in range(n):
        if lst[i] > lst[Ma]:
            Ma = i
            if temp:
                temp = []
        elif lst[i] == lst[Ma] and i != 0:
            temp.append(i)
    if Ma == 0 and len(temp) == 0:
        return [lst[0]] + change(lst[1:], N)
    else:
        if temp:
            new_lst = sorted(lst, reverse=True)
            if lst == new_lst:
                return lst
            else:
                lst[0], lst[Ma] = lst[Ma], lst[0]
                return [lst[0]] + change(lst[1:], N)
        else:
            lst[0], lst[Ma] = lst[Ma], lst[0]
            return [lst[0]] + change(lst[1:], N - 1)

for tc in range(1, int(input())):
    numbers, N = input().split()
    N = int(N)
    numbers = list(map(int, numbers))
    print('#{} {}'.format(tc, ''.join(map(str, change(numbers, N)))))


# def s_sort(ls, N, cnt, change):
#     if cnt == change:
#         return ls
#     elif N == len(li):
#         if (change-cnt) % 2:
#             ls[0], ls[1] = ls[1], ls[0]
#             return ls
#         return ls
#     else:
#         max_n = 0
#         for i in range(N, len(li)):
#             if ls[i] > ls[max_n]:
#                 max_n = i
#         ls[N], ls[max_n] = ls[max_n], ls[N]
#         cnt += 1
#         return s_sort(ls, N+1, cnt, change)
#
#
# for tc in range(1, int(input())+1):
#     li, change = input().split()
#     li = list(map(int, li))
#     change = int(change)
#     cnt = 0
#     a = s_sort(li, 0, 0, change)
#     ans = 0
#     dup = 0
#     for i in range(len(a)-1, -1, -1):
#         ans += a[i] * (10 ** dup)
#         dup+=1
#     print('#{} {}'.format(tc, ans))


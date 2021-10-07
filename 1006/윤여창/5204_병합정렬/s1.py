def part(lst):

    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left_lst = part(lst[:mid])
    right_lst = part(lst[mid:])
    return merge(left_lst, right_lst)


def merge(left_lst, right_lst):
    global cnt
    result = []

    if left_lst[-1] > right_lst[-1]:
        cnt += 1

    while len(left_lst) > 0 or len(right_lst) > 0:
        if len(left_lst) > 0 and len(right_lst) > 0:
            if left_lst[0] <= right_lst[0]:
                result.append(left_lst[0])
                left_lst = left_lst[1:]
            else:
                result.append(right_lst[0])
                right_lst = right_lst[1:]

        elif len(left_lst) > 0:
            result.append(left_lst[0])
            left_lst = left_lst[1:]
        elif len(right_lst) > 0:
            result.append(right_lst[0])
            right_lst = right_lst[1:]

    return result


T = int(input())

for tc in range(1, T + 1):
    cnt = 0
    N = int(input())
    lst = list(map(int, input().split()))
    Data = part(lst)

    print('#{} {}'.format(tc,cnt))
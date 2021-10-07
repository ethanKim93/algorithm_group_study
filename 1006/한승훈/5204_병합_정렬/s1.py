import sys
sys.stdin = open('sample_input.txt')


def merge_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    mid = n//2
    l = merge_sort(lst[:mid])
    r = merge_sort(lst[mid:])
    return merge(l, r)


def merge(l, r):
    global l_cnt
    l_n, r_n = len(l), len(r)
    result = []
    i = j = 0
    if l[-1] > r[-1]:
        l_cnt += 1
    while l_n > i or r_n > j:
        if l_n > i and r_n > j:
            if l[i] <= r[j]:
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1
        elif l_n > i:
            result.append(l[i])
            i += 1

        elif r_n > j:
            result.append(r[j])
            j += 1
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    l_cnt = 0
    sorted_nums = merge_sort(nums)
    print('#{} {} {}'.format(tc, sorted_nums[N//2], l_cnt))

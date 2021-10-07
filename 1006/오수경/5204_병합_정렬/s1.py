import sys
sys.stdin = open('sample_input.txt')


def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1

    merge_lst = []
    l, r = 0, 0
    while (l < len(left)) and (r < len(right)):
        if left[l] < right[r]:
            merge_lst.append(left[l])
            l += 1
        elif left[l] == right[r]:
            merge_lst += [left[l], right[r]]
            l += 1
            r += 1
        else:
            merge_lst.append(right[r])
            r += 1


    # 리스트를 처음에 += 로 사용했더니 Runtime Error가 났다
    # += 보다 extend() 가 더 빠르다!!!!!!

    merge_lst.extend(right[r:])
    merge_lst.extend(left[l:])
    return merge_lst


def mergesort(lst, N):
    if len(lst) <= 1:
        return lst

    mid = N // 2
    left = lst[:mid]
    right = lst[mid:N]
    left = mergesort(left, len(left))
    right = mergesort(right, len(right))
    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    cnt = 0

    print('#{} {} {}'.format(tc, mergesort(L, N)[N//2], cnt))
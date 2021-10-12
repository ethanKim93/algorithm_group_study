# runtime error 해결하기
def binary_search(arr, l, r, target):
    global cnt
    if l > r:
        return
    m = (l + r) // 2

    if arr[m] > target:
        return binary_search(arr, l, m-1, target)
    elif arr[m] < target:
        return binary_search(arr, m+1, r, target)
    else:
        cnt += 1
        return


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0

    for num in B:
        binary_search(A, 0, len(A)-1, num)
    print('#{} {}'.format(tc, cnt))
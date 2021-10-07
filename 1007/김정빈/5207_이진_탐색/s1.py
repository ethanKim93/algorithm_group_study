import sys
sys.stdin = open("sample_input.txt")

def binarySearch(n, arr, key):
    global cnt
    s, e = 0, n-1
    dir = 0 # -1==왼 1==오
    while s <= e:
        mid = (s + e)//2
        if arr[mid] == key:
            cnt += 1
            break
        elif arr[mid] > key:
            e = mid - 1
            if dir == -1: break
            dir = -1
        else:
            s = mid + 1
            if dir == 1: break
            dir = 1
    return # 검색 실패

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))

    cnt = 0
    for k in b:
        binarySearch(A, a, k)
    print('#{} {}'.format(tc, cnt))
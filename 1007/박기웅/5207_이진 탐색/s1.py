import sys
sys.stdin = open('sample_input.txt')

def binary_search(obj, l, r):
    global ans
    cnt = 0                       # cnt = 1 -> 오른쪽, cnt = -1 -> 왼쪽
    while l <= r:
        mid = (l+r)//2
        if A[mid] == obj:
            ans += 1
            return                
        elif A[mid] < obj:        # 오른쪽에서 찾음
            l = mid+1       
            if cnt == 1: return   # 오른쪽 -> 오른쪽일 경우 실패
            cnt = 1
        else:                     # 왼쪽에서 찾음
            r = mid-1
            if cnt == -1: return  # 왼쪽 -> 왼쪽일 경우 실패
            cnt = -1
    return                        # 못찾은 경우 return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))     # sorted 적용...input이 정렬되있는거 아니었나...?
    B = list(map(int, input().split()))
    ans = 0
    for b in B:
        binary_search(b, 0, len(A)-1)
    print('#{} {}'.format(tc, ans))

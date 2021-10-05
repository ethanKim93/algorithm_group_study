import sys
sys.stdin = open("input.txt")
#5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임
def is_baby(arr):
    arr.sort()
    for i in range(len(arr)-3):
        # if arr[i]+2 == arr[i+1]+1 == arr[i+2]:
        if arr[i]+1 in arr and arr[i]+2 in arr:
            return True
        if arr[i] == arr[i+1] == arr[i+2]:
            return True

T = int(input())
for tc in range(1, T+1):
    cds = list(map(int, input().split()))
    p1, p2 = [], []
    res = '0'
    for i in range(0,12,2):
        p1.append(cds[i])
        p2.append(cds[i+1])
        if len(p1) >= 3:
            if is_baby(p1):
                res = '1'
                break
            if is_baby(p2):
                res = '2'
                break
    print('#{} {}'.format(tc, res))
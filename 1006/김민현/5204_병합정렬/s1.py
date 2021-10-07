import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def mergesort(arr):
    global cnt
    n = len(arr)
    if n == 1:
        return arr
    temp1 = mergesort(arr[:n//2])
    temp2 = mergesort(arr[n//2:n])

    #왼쪽 끝 값이 오른쪽 끝값보다 큰 경우
    if temp1[-1] > temp2[-1]:
        cnt += 1
    return sorted(temp1+temp2)

for tc in range(1,T+1):
    N = int(input())
    ai = list(map(int,input().split()))
    cnt = 0
    ans = mergesort(ai)
    print('#{} {} {}'.format(tc,ans[N//2],cnt))
# 교재에 나온대로 left, right 배열을 계속 만들어나가는 식으로 만들면, 시간초과 + 메모리초과
# -> 인덱스 조작으로 해결

import sys
sys.stdin = open('sample_input.txt')

def merge_sort(s,e):
    if s==e:
        return
    mid = (s+e-1)//2
    merge_sort(s,mid)
    merge_sort(mid+1,e)

    res = [0] * (e-s+1)
    merge(s,mid+1,mid,e,res)

    t = 0
    for m in range(s,e+1):      # 정렬 끝낸 res 배열을 li 배열에 복사
        li[m] = res[t]
        t += 1
    return

def merge(i,j, mid, e, res):
    global cnt
    t = 0
    if li[mid] > li[e]:     # 왼쪽 마지막값이 오른쪽 마지막값보다 크면, 오른쪽 정렬이 먼저끝나므로 cnt + 1
        cnt += 1
    while i <= mid or j <= e:
        if i <= mid and j <= e:
            if li[i] <= li[j]:
                res[t] = li[i]      # append는 시간초과나므로 res 배열에 추가하는 것도 인덱스 조작으로 해결
                i += 1
                t += 1
            else:
                res[t] = li[j]
                j += 1
                t += 1
        elif i <= mid:
            res[t] = li[i]
            i += 1
            t += 1
        elif j <= e:
            res[t] = li[j]
            j += 1
            t += 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = 0
    li = list(map(int,input().split()))
    merge_sort(0,len(li)-1)
    print('#{} {} {}'.format(tc,li[N//2],cnt))
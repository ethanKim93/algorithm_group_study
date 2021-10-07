import sys
sys.stdin = open('input.txt')

def lining(arr):
    global cnt
    if len(arr)==1:
        return arr
    mid = len(arr)//2
    left_arr = lining(arr[:mid])
    right_arr = lining(arr[mid:])
    if left_arr[-1]>right_arr[-1]:
        cnt += 1

    merged_arr = []
    l = r = 0
    while l<len(left_arr) and r<len(right_arr):
        if left_arr[l] < right_arr[r]:
            merged_arr.append(left_arr[l])
            l += 1
        else:
            merged_arr.append(right_arr[r])
            r += 1
    merged_arr += left_arr[l:]
    merged_arr += right_arr[r:]
    return merged_arr

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    print('#{}'.format(tc),end=' ')
    print(lining(num)[N//2],cnt)


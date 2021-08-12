import sys
sys.stdin = open("sample_input.txt")

def binary(Page, key):
    start = 1
    end = Page
    cnt = 0
    while start <= end:
        mid = (start + end)//2
        if mid == key:
            break
        elif mid > key:
            end = mid
            cnt+=1
        else:
            start = mid
            cnt+=1
    return cnt

T = int(input())
for tc in range(1,T+1):
    P, A, B = map(int,input().split())
    if binary(P,A) < binary(P,B):
        print('#{} A'.format(tc))
    elif binary(P,A) > binary(P,B):
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))

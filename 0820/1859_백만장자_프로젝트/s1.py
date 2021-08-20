import sys
sys.stdin=open('input.txt')
T=int(input())
for tc in range(1,T+1):
    N= int(input())
    arr=list(map(int,input().split()))
    save=0
    max=arr[len(arr)-1]
    for i in range(len(arr)-1,-1,-1):
        if max>arr[i]:
            save+=(max-arr[i])
        elif max<=arr[i]:
            max=arr[i]

    print('#{} {}'.format(tc,save))

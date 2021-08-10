import sys
sys.stdin=open('input.txt')
width=0

heights=[]

T= int(input())

for tc in range(1,T+1):
    temp = 0

    arr = []
    diff = []
    width=(int(input()))
    heights = list(map(int, input().split()))
    for n in heights:
        if n==0:
            continue
        else : arr.append(n)

    for k in range(len(arr)-1):
        if(arr[k]>arr[k+1]):
            for m in range(arr[k],arr[k+1],-1):
                cac = 0
                cac=m-arr[k+1]
                cac=arr[k+1]+cac
                diff.append(cac)
        else: continue
    print(diff)
    for q in diff:
        if q>temp:
            temp=q


    print(temp)










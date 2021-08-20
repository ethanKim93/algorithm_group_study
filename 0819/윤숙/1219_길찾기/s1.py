import sys

sys.stdin = open('input.txt')
T = 10
for tc in range(1, T + 1):
    t, N = map(int, input().split())
    arr=list(map(int,input().split()))
    arrLink=[[99]*6 for _ in range(2)]
    print(t,N)
    print(arr)

    # for i in range(0,len(arr),2):
    #     for j in range(1,len(arr)-1,2):
    #         if arrLink[arr[i]]<arr[j]:
    #             arrLink[arr[i]]=arr[j]
    #

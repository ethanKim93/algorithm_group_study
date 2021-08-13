import sys
sys.stdin=open('sample_input.txt')
T= int(input())

for tc in range(1,T+1):

    while True:
        N,K= map(int,input().split())
        if 1<=N<=12 and 1<=K<=100:
            break

    arr=list(range(1,13))
    for n in range(1, N + 1):
        arr.append(n)

    result=0
    for i in range(1, 1 << 12):
        sum = 0
        C = 0
        arr_s=[]
        for j in range(13):
            if i & (1 << j):
                arr_s.append(arr[j])
                C+=1
        for k in range(len(arr_s)):
            sum += arr_s[k]

        if sum == K and C==N:
             result+=1

    print('#{} {}'.format(tc,result))










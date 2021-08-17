import sys
sys.stdin=open('input.txt')
T=int(input())
for tc in range(1,T+1):
    S1=input()
    S2=input()


    S1_arr = []
    for i in S1:
        S1_arr.append(i)



    S2_arr=[]
    for i in S2:
        S2_arr.append(i)

    Count = [0] * len(S1_arr)


    for i in range(0,len(S1_arr)):
        for j in range(0,len(S2_arr)):
            if S1_arr[i]==S2_arr[j]:
                Count[i]+=1

    maxV = 0;
    for i in range(len(Count)):
        if Count[i]> maxV:
            maxV=Count[i]


    print('#{} {}'.format(tc,maxV))



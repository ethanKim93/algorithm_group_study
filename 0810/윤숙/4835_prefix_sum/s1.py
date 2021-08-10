import sys
sys.stdin=open('input.txt')

T=int(input())

for tc in range(1,T+1):

    n,sli=map(int,input().split())

    list_n =list(map(int,input().split()))


    sum_list=[]
    slicing = []
    for i in range(len(list_n)-sli+1):
        sum = 0
        slicing_list=list_n[i:i+sli]

        for i in slicing_list:
            sum+=i
        sum_list.append(sum)

    flag_mx=sum_list[0]
    for mx in sum_list:
        if mx > flag_mx:
            flag_mx=mx

    flag_mn=sum_list[0]
    for mn in sum_list:
        if mn < flag_mn:
            flag_mn=mn


    print('#{} {}'.format(tc,flag_mx-flag_mn))


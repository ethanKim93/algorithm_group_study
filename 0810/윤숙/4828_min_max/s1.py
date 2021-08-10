import sys
sys.stdin=open('input.txt')
T=int(input())

numbers=[]
for tc in range(1,T+1):
    Num=int(input())
    numbers=list(map(int,input().split()))

    max=0
    min=9999999
    for i in numbers:
        if max<i:
            max=i
        if min>i:
            min=i

    print('#{} {}'.format(tc,max-min))

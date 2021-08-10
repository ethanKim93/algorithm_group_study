import sys
sys.stdin=open('input.txt')

T=int(input())

for tc in range(1,T+1):
    count = [0] * 10
    n=int(input())
    card_number=list(map(int, input()))

    for i in card_number:
        count[i]+=1
    arr=[]
    max=0
    for n in count:
        if max<n:
            max=n
    for n in range(len(count)):
        if max==count[n]:
            arr.append(n)
    arr_max=0
    for n in arr:
        if arr_max<n:
            arr_max=n


    print('#{} {} {}'.format(tc, arr_max, count[arr_max]))


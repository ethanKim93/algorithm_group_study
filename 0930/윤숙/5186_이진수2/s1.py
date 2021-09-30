import sys
sys.stdin=open('input.txt')
T=int(input())
for tc in range(1,T+1):
    num=float(input())
    op=-1
    cnt=0
    p=[]
    while num<1:
        if num==1:
            break
        num=num*2
        cnt+=1

        if num>1:
            num=num-1
            p.append(1)
        elif num==1:
            p.append(1)
        else:
            p.append(0)
    print('#{} '.format(tc), end='')

    if len(p)>=13:
        print('overflow')
    else:
        p=''.join(map(str,p))
        print(p)
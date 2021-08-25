import sys
sys.stdin=open('input.txt')
T=10
for tc in range(1,T+1):
    N=int(input())
    queue=list(map(int,input().split()))
    # print(queue)
    flag=0

    while True:
        if flag==1:
            break

        for i in range(1,6):
            tmp=queue.pop(0)
            tmp=tmp-i
            if tmp <= 0:
                tmp = 0
                flag=1
            queue.append(tmp)
            if flag==1:
                break


    result=' '.join(map(str,queue))
    print('#{} {}'.format(N, result))
import sys
sys.stdin=open('input.txt')
T= int(input())
for tc in range(1,T+1):

    V=int(input())
    heap_list=list(map(int,input().split()))
    heap_list.insert(0,0)


    for i in range(V+1):
        p=V//2
        while p!=1:
            if heap_list[i]<heap_list[i//2]:
                tmp=heap_list[i//2]
                heap_list[i//2]=heap_list[i]
                heap_list[i]=tmp
                p//=2
                i//=2
            else:
                break

    print(heap_list)
    cac = 0
    while V!=1:
        V=V//2
        cac+=heap_list[V]
    print('#{} {}'.format(tc,cac))

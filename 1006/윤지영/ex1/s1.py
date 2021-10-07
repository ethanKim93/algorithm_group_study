import sys
sys.stdin = open('input.txt')

def quicky(l, L, r):
    if L < r :
        s = partition(l,L,r)
        quicky(l,L,s-1)     # 피봇기준 왼쪽
        quicky(l,s+1,r)     # 피봇기준 오른쪽

def partition(l,L,r):
    p = l[L]        # 제일 왼쪽값을 피봇으로
    i,j = L,r
    while i <= j:
        while i <= j and l[i] <= p:
            i += 1
        while i <= j and l[j] >= p:
            j -= 1
        if i < j:
            l[i], l[j] = l[j], l[i]
    l[L],l[j] = l[j], l[L]                # 제일 왼쪽값이 피봇이므로 j인덱스와 교환 / l[L]을 p에 할당했지만, 리스트 내의 값을 교환해야하므로 p로 작성하면 안됨
    return j

T = int(input())
for tc in range(1,T+1):
    li = list(map(int,input().split()))
    quicky(li,0,len(li)-1)
    print(li)

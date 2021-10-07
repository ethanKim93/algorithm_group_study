import sys
sys.stdin = open('sample_input.txt')

def lining(num,s,e):
    pivot = num[e]
    under = s-1
    for i in range(s,e):
        if num[i]<pivot:
            under += 1
            num[i],num[under] = num[under],num[i]
    num[under+1],num[e] = num[e],num[under+1] # 피봇을 가운데로 보냄
    return under+1

def quick(li,s,e):
    if s<e:
        standard = lining(li,s,e)
        quick(li,s,standard-1)
        quick(li,standard+1,e)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split()))
    quick(num,0,N-1)
    print('#{} {}'.format(tc,num[N//2]))

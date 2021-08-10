import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))

    for end in range(len(a)-1,0,-1):
        for i in range(0,end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]

    result = a[len(a)-1] - a[0]

    print('#{} {}'.format(tc, result))

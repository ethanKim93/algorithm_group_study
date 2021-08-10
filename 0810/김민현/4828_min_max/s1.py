import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ai = list(map(int,input().split()))
    a_max = ai[0]
    a_min = ai[0]
    for i in ai:
        if a_max < i:
            a_max = i
        if a_min > i:
            a_min = i
    result = a_max - a_min

    print('#{0} {1}'.format(tc,result))


import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ai = list(map(int,input().split()))
    
    for i in range(0,10,2):
        max_ai = ai[i]
        min_ai = ai[i]
        for j in range(i,len(ai)):
            if max_ai < ai[j]:
                max_ai = ai[j]
                ai[i],ai[j] = ai[j],ai[i]
            if min_ai > ai[j]:
                min_ai = ai[j]
                ai[i+1],ai[j] = ai[j],ai[i+1]
    
    
    print('#{0}'.format(tc),end=' ')
    print(*ai[0:10])

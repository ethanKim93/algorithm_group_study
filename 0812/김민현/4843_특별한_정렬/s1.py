import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ai = list(map(int,input().split()))
    
    for i in range(0,10,2): # 2간격
        max_ai = ai[i]
        min_ai = ai[i]
        
        for j in range(i,len(ai)):
            if max_ai < ai[j]:# 가존보다 높은 값 찾기
                max_ai = ai[j] 
                ai[i],ai[j] = ai[j],ai[i] # i위치와 가장 높은값 자리 바꿈
            if min_ai > ai[j]:# 기존보다 낮은 값 찾기
                min_ai = ai[j] 
                ai[i+1],ai[j] = ai[j],ai[i+1] # i+1과 가장 낮은 값 찾기
    
    
    print('#{0}'.format(tc),end=' ')
    print(*ai[0:10])

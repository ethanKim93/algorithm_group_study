import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ai = list(map(int,input().split()))
    
    for i in range(0,10,2): # 2간격
        max_i = i
        min_i = i
        
        for j in range(i,len(ai)):
            if ai[max_i] < ai[j]:# 가존보다 높은 값 찾기
                 # i위치와 가장 높은값 자리 바꿈
            if ai[min_i] > ai[j]:# 기존보다 낮은 값 찾기
                min_i = j
            ai[i],ai[max_i] = ai[max_i],ai[i]
            ai[i+1],ai[min_i] = ai[min_i],ai[i+1] # i+1과 가장 높은 값 찾기
    
    
    print('#{0}'.format(tc),end=' ')
    print(*ai[0:10])

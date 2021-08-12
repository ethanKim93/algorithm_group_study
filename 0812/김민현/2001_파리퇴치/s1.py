import sys
sys.stdin = open('input.txt')

T = int(input())
'''
# M=2
dx = [0,1,0,1]
dy = [0,0,1,1]

M = 3
dx = [0,1,2,0,1,2,0,1,2]
dy = [0,0,0,1,1,1,2,2,2]
'''

for tc in range(1,T+1):
    N,M = map(int,input().split())   
    hall = []
    for k in range(N):
        hall.append(list(map(int,input().split())))
    
    dx = []
    dy = []
    for i in range(M):
        dx.append(i)
        for j in range(M):
            dy.append(i)
    dx = dx*M

    high_score = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
           
            result = 0
            for k in range(M*M):
                x = i + dx[k]
                y = j + dy[k]
                result += hall[x][y]
            if result > high_score:
                high_score = result
           
    print('#{} {}'.format(tc,high_score))
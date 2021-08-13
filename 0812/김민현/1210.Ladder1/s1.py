import sys
sys.stdin = open('input.txt')

dx = [-1,0,0]
dy = [0,-1,1]

dir = 0 # 0:위 ,1:좌 ,2:우

for i in range(1,11):
    tc = int(input())
    ladder = []
    for bar in range(100):
        arr = list(map(int,input().split()))
        ladder.append(arr)
    end_i = 0
    end_j = 0
    # 시작 위치값 찾기
    for i in range(len(ladder)):
        for j in range(len(ladder)):
            if ladder[i][j] == 2:
               end_i = i
               end_j = j

    while end_i > 0: # 맨 위쪽에 올라올때까지 반복
        if dir == 0 : #이전 방향이 위일때
            if end_j != 0 and ladder[end_i + dx[1]][end_j + dy[1]] == 1 :
                dir = 1
            elif end_j != 99 and ladder[end_i + dx[2]][end_j + dy[2]] == 1:
                dir = 2
            else:
                dir = 0
        elif dir == 1:#이전 방향이 좌측일때
            if end_j != 0 and ladder[end_i + dx[1]][end_j + dy[1]] == 1: #좌측 벽이 아니고 , 계속 좌측이 1이라면
                dir = 1
            else:
                dir = 0
        else:#이전 방향이 우측일때
            if end_j != 99 and ladder[end_i + dx[2]][end_j + dy[2]] == 1: #우측 벽이 아니고, 계속 우측이 1이라면
                dir = 2
            else:
                dir = 0
        end_i = end_i + dx[dir]
        end_j = end_j + dy[dir]
    print('#{} {}'.format(tc,end_j))
print()
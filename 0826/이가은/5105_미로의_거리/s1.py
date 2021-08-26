import sys
sys.stdin = open('sample_input.txt')

def miro_find(Sy,Sx):
    d = [[-1,0], [0,1], [1,0], [0,-1]]

    que = [[Sy, Sx]]
    distance = [[0]*(N+1) for _ in range(N+1)]
    distance[Sy][Sx] = 1

    while que:
        my, mx = que.pop(0)

        for i in range(4):
            ny = my + d[i][0]
            nx = mx + d[i][1]

            if -1 < ny < N and -1 < nx < N and (miro[ny][nx] == 0 or miro[ny][nx] == 3) and not(distance[ny][nx]):
                que.append([ny, nx])
                if miro[ny][nx] == 3:
                    return distance[my][mx] -1
                else:
                    miro[ny][nx] = 1
                    distance[ny][nx] = distance[my][mx] + 1

    return 0


T = int(input())

for tc in range(T):
    N = int(input())
    miro = [list(int(char) for char in input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                Sy = i
                Sx = j

    print('#{} {}'.format(tc+1,miro_find(Sy,Sx)))

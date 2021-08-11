import sys
sys.stdin = open('input.txt')

N = int(input())
# cnt = [int(sys.stdin.readline())]
# for i in range(1,N):
#     cnt.append(int(sys.stdin.readline()))
cnt = 1
li = [[0]*N for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
while cnt <= N*N:
    for i in range(0, N):
        for j in range(-1, N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if (0 <= ni < N) and (0 <= nj < N) and (li[ni][nj] == 0):
                    li[ni][nj] = cnt
                    cnt += 1
                    i, j = ni, nj
                else:
                    k = (k+1)%4
print(li)


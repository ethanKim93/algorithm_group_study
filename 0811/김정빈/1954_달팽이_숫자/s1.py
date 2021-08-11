import sys
sys.stdin = open(input.txt)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 5
cnt = 1
i, j = 0, -1
k = 0
while cnt<= N*N:
    ni, nj = i+di[k], j+dj[k]
    if ni, nj 가 유효하고 and A[ni][nj]
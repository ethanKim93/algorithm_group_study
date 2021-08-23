import sys
sys.stdin = open("input.txt")

def mat_count(arr,i,j):
    global cnt
    global result
    global flag
    global K
    if cnt == K:
        result += 1
    if flag == False:
        if matrix[i][j] == 0:
            pass
        else:
            flag = True
            cnt += 1
    else:
        if matrix[i][j] == 0:
            flag = False
            cnt = 0
        else:
            cnt += 1


for tc in range(1,int(input())+1):
    N,K = map(int,input().split())

    matrix = []
    for _ in range(N):
        mat = list(map(int,input().split()))
        mat.append(0)
        matrix.append(mat)
    matrix.append([0]*N)

    result = 0
    for i in range(N+1):
        cnt = 0
        flag = False
        for j in range(N-K):
            mat_count(matrix,i,j)
            mat_count(matrix,j,i)

    print(result)
import sys
sys.stdin = open('sample_input.txt')

def maze(mat, i, j):
    global result
    if i == ei and j == ej:
        result = 1
        return
    if mat[i-1][j] == 1:
        pass
    else:
        mat[i-1][j] = 1
        maze(mat,i-1,j)
    if mat[i+1][j] == 1:
        pass
    else:
        mat[i+1][j] = 1
        maze(mat,i+1,j)
    if mat[i][j+1] == 1:
        pass
    else:
        mat[i][j+1] = 1
        maze(mat,i,j+1)
    if mat[i][j-1] == 1:
        pass
    else:
        mat[i][j-1] = 1
        maze(mat,i,j-1)






T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[1]*(N+2)] + [[1] + list(map(int, list(input()))) + [1] for _ in range(N)] + [[1]*(N+2)]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 2:
                si, sj = i, j
            if matrix[i][j] == 3:
                ei, ej = i, j
    result = 0
    maze(matrix,si,sj)
    print('#{} {}'.format(tc, result))
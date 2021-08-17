import sys
sys.stdin = open('input.txt')

def palin(mat):
    # for long in range(len(mat),0,-1):
    flag1 = 0
    for long in range(1, len(mat)+1):
        flag = 0
        for i in range(len(mat)-long+1):
            for j in range(len(mat)-long+1):
                for k in range(long):
                    if mat[i+k][j:j+long] == mat[i+k][j:j+long][::-1]:
                        # print('row', k, mat[i+k][j:j+long])
                        flag = 1
                        # return(long)
                    col = ''
                    for c in range(i, i+long):
                        col += mat[c][j+k]
                    if col == col[::-1]:
                        # print('col', k, col)
                        flag = 1
                        # return(long)
        if not flag:
            if not flag1:
                return(long-2)
        flag1 = flag


T = 10

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(100)]
    # print(matrix)

    print('#{} {}'.format(tc,palin(matrix)))
    #
    # for i in range(100):
    #     for j in range(100):
    #         for long in range(100)
    #
    #
    # for long in range(100, 0, -1):
    #
    #
    #
    #     for i in range(100-long+1):
    #         for j in range(100-long+1):
    #             for k in range(long):
    #                 if matrix[i+k][j:j+long] == matrix[i+k][j:j+long][::-1]:
    #                     print(matrix[i+k][j:j+long])
    #                     result = long
    #                     break
    #                 if matrix[j+k][i:i+long] == matrix[j+k][i:i+long][::-1]:
    #                     print(matrix[j+k][i:i+long])
    #                     result = long
    #                     break
    #                 if result:
    #                     break
    #         if result:
    #             break
    #     if result:
    #         break
    # print(result)
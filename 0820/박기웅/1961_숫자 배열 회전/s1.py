import sys
sys.stdin = open("input.txt")
'''
90도를 회전하는 함수하나 만들어서 중복 적용
코드에 중복이 좀 있는것 같아 줄일 수 있는 방법이 있을까?
'''
def rot90(mat):
    new_mat = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_mat[j][N - i - 1] = mat[i][j]
    return new_mat

for tc in range(1, int(input())+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    mat9 = rot90(mat)
    mat18 = rot90(mat9)
    mat27 = rot90(mat18)
    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(map(str, mat9[i])), end=' ')
        print(''.join(map(str, mat18[i])), end=' ')
        print(''.join(map(str, mat27[i])), end=' ')
        print()

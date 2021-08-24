import sys
sys.stdin = open('sample_input.txt')

def check(mat, N, row, subsum):
    global minimum
    global flag
    print(stack)
    # print(subsum, minimum, stack, row)
    if subsum > minimum and flag:
        return
    if row == N-1:
        if not flag:
            minimum = subsum + mat[row][stack[0]]
            flag = True
        elif minimum > subsum + mat[row][stack[0]]:
            minimum = subsum + mat[row][stack[0]]
            print('#last {}'.format(subsum + mat[row][stack[0]]))
            return subsum + mat[row][stack[0]]
        else:
            return
    for i in stack:
        stack.remove(i)
        # print( N, row+1, mat[row][i])
        check(mat, N, row+1, subsum + mat[row][i])
        stack.insert(i,i)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    stack = [False] * N
    minimum = 1000
    subsum = 0
    flag = False
    print(check(matrix, N, 0, 0))
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 가로 list 만들기
    arr = []
    for _ in range(N):
        string = input()
        arr.append(string)

    # 세로 list 만들기
    colArr = []
    colStr = ''
    for i in range(N):
        colStr = ''
        for j in range(N):
            colStr += arr[j][i]
        colArr.append(colStr)

    result = ''
    while result == '':
        # 가로 찾기
        for row in arr:
            for i in range(0, N-M+1):
                for plus in range(0, M//2):
                    if row[i+plus] != row[i+M-1-plus]:
                        break
                else:
                    result = row[i:i+M]

        # 세로 찾기
        for col in colArr:
            for i in range(0, N-M+1):
                for plus in range(0, M//2):
                    if col[i+plus] != col[i+M-1-plus]:
                        break
                else:
                    result = col[i:i+M]

    print('#{} {}'.format(tc, result))

    # arr = [list(input()) for _ in range(N)]
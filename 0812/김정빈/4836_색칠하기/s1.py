import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = [[0]* 10 for _ in range(10)]
    purple = 0
    for n in range(N):
        r1, c1, r2, c2, color = map(int,input().split())
        if color == 1: #빨
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    box[i][j] += 1
        if color == 2: #파
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if box[i][j] == 1:
                        purple += 1
                    else:
                        box[i][j] += 2

    print('#{} {}'.format(tc, purple))


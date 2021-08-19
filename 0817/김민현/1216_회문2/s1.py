#실행 시간 : 3.90915s

import sys
sys.stdin = open("input.txt")

for _ in range(1,11):
    tc = int(input())
    mat = [list(input()) for _ in range(100)]

    longest = 1
    for k in range(0,100):
        for i in range(100):
            for j in range(100-k+1):
                flag_x = True
                flag_y = True
                for c in range(k//2):
                    if mat[i][j+c] == mat[i][j+k-c-1]:
                        pass
                    else:
                        flag_x = False

                    if mat[j+c][i] == mat[j+k-c-1][i]:
                        pass
                    else:
                        flag_y = False

                if flag_x == True and longest < k:
                    longest = k
                if flag_y == True and longest < k:
                    longest = k


    print('#{} {}'.format(tc,longest))

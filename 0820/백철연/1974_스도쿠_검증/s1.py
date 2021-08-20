import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 0
    #가로 검정
    for w in range(9):
        for q in range(9):
            if len(set(arr[w][q])) != 9:
                result = 1
            else:
                result = 0
            print(result)
    #세로 검정
    for w in range(9):
        for q in range(9):
            if len(set(arr[w][q])) != 9:
                result = 1
            else:
                result = 0

    # 3x3 검정
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for w in range(3):
                for q in range(3):
                    if len(set(arr[w][q])) != 9:
                        result = 1
                    else:
                        result = 0
    if result == 0:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, 1))
#################################################### 미완성


import sys

sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]  #0이 입력이안됨...ㅠㅠㅠㅠㅠ


    Startpoint = N // 2
    i = 0
    j = 0
    sum = 0
    # st=2
    for i in range(Startpoint, -1, -1):  # 2,1,0
        for j in range(i, N - i):  # 2~3,1~4,0~5
                sum += arr[Startpoint - i][j]

    for i in range(1, Startpoint+1):  # 1,2
        for j in range(i, N - i):
                sum += arr[Startpoint + i][j]

    print('#{} {}'.format(tc,sum))

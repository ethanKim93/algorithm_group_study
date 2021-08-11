import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    #우하향 아래방향 대각선의 합
    maxV1 = 0
    s1 = 0

    for i in range(100):
        for j in range(100):
            if i == j:
                s1 += arr[i][j]
    if maxV1 < s1:
        maxV1 = s1

    #print(maxV1)

    s2 = 0 # 왼쪽아래 대각선의 합
    maxV2 = 0

    for i in range(100):
        s2 += arr[i][99-i]
    if maxV2 < s2:
        maxV2 = s2
    #print(maxV2)

    # #
    # # s2 = 0 # 왼쪽아래 대각선의 합
    # # maxV2 = 0
    # #
    # # for i in range(100):
    # #     s2 += arr[i][99-i]
    # # if maxV2 < s2:
    # #     maxV2 = s2
    # # print(maxV2)
    # #

    # 행의합
    maxV3 = 0

    for i in range(100):
        s3 = 0
        for j in range(100):
            s3 += arr[i][j] # i행의 합
        if maxV3 < s3:
            maxV3 = s3
    #print(maxV3)


    #열의합
    maxV4 = 0

    for j in range(100):
        s4 = 0
        for i in range(100):
            s4 += arr[i][j]
        if maxV4 < s4:
            maxV4 = s4
    #print(maxV4)

    result =[maxV1,maxV2,maxV3,maxV4]

    max_re = result[0]
    for i in range(1, len(result)):
        if max_re < result[i]:
            max_re = result[i]
    print(max_re)


for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    maxV = 0
    s1 = 0
    for i in range(100):
        s += arr[i][i] # 우하향 아래방향 대각선 원소

    for i in range(100):
        for j range(100):
            if i==j:
                s += arr[i][j]
    if maxV < s:
        maxV = s
    maxV = s

    s2 = 0 # 왼쪽아래 대각선의 합
    for i in range(100):
        s2 += arr[i][99-i]
    if maxV < s:
        maxV = s

    s1 = 0
    s2 = 0
    for i in range(100):
        s1 += arr[i][i]
        s2 += arr[i][99-1]       # 같은 인덱스를 사용해도 내부의 연산이 독립적이라면 하나의 for에 써도 됨

    maxV = s1        # maxV = max(s1, s2)
    if maxV < s2:
        maxV = s2


    # 행의합
    for i in range(100):
        s = 0
        for j in range(100):
            s += arr[i][j] # i행의 합
        if maxV < s:
            maxV = s

    #열의합
    for j in range(100):
        s = 0
        for i in range(100):
            s += arr[i][j]
        if maxV < s:
            maxV = s

    #행의합과 열의합
    for i in range(100):
        s1 = 0 # 행의 합
        s2 = 0 # 열의 합
        for j in range(100):
            s1 += arr[i][j] # 행우선 탐색
            s2 += arr[j][i] # 열우선 탐색
        if maxV < s1:
            maxV = s1
        if maxV < s2:
            maxV = s2
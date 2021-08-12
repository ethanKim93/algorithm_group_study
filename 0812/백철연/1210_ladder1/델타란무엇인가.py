arr = [[1, 2, 3, 3],
       [3, 7, 5, 3],
       [3, 5, 4, 1],
       [1, 5, 4, 6]]
dx = [0, 0, -1, 1]  # 상 하 좌 우
dy = [-1, 1, 0, 0]

for x in range(1, len(arr) - 1):
    for y in range(1, len(arr[x]) - 1):
        print(arr[x][y])
        newlist = []

        for i in range(4):
            testx = x + dx[i]
            testy = y + dy[i]
            newlist.append(arr[testx][testy])

        print("상하좌우", newlist)
        print()
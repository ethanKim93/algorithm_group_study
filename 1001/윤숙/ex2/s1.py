babygin = [[1, 2, 3, 7, 8, 3], [6, 6, 7, 7, 6, 7], [0, 5, 4, 0, 6, 0], [1, 0, 1, 1, 2, 3]]


def is_babyjin(p):
    global flag
    tri = 0
    run = 0
    for i in range(0, 6, 3):
        if (p[i] == p[i + 1] == p[i + 2]):
            tri += 1
        elif (p[i + 1] == p[i] + 1 and p[i + 2] == p[i] + 2):
            run += 1
    if tri + run == 2:
        flag = 'Baby_Gin'


def permutation(cnt):
    global flag
    if cnt == n:
        is_babyjin(p)
        return
    else:
        for j in range(n):
            if visited[j]:
                continue
            visited[j] = 1
            p[cnt] = arr[j]
            permutation(cnt + 1)
            visited[j] = 0


for i in range(len(babygin)):
    p = [0, 0, 0, 0, 0, 0]
    visited = [0] * (len(babygin[i]))
    arr = babygin[i]
    cnt = 0
    n = 6
    flag = 'Lose'
    permutation(cnt)
    print('{} {}'.format(i + 1, flag))

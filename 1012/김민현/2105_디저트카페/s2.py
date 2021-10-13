#인터넷 풀이
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]


# k는 방향, n은 진행한 칸수
def f(i, j, k, n):
    global si, sj, maxV
    # 출발점에 도착한경우
    if k == 3 and i == si and j == sj:
        if maxV < n:
            maxV = n
    elif i < 0 or i >= N or j < 0 or j >= N:
        return
    # 숫자가 겹친경우
    elif arr[i][j] in U:
        return
    else:
        U.append(arr[i][j])
        # 오른쪽 방향 그대로 가거나 왼쪽으로 꺾었을 경우에
        if k == 0 or k == 1:
            f(i + di[k], j + dj[k], k, n + 1)
            # k+1방향
            f(i + di[k + 1], j + dj[k + 1], k + 1, n + 1)
        elif k == 2:
            # 출발점을 향하는게 아님
            if i + j != si + sj:
                f(i + di[2], j + dj[2], k, n + 1)
            else:
                f(i + di[3], j + dj[3], k + 1, n + 1)
        # k가 3일때는 직진한다.
        else:
            f(i + di[3], j + dj[3], k, n + 1)

        U.remove(arr[i][j])


T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    maxV = -1
    U = []
    for i in range(N):
        for j in range(1, N - 1):
            si = i
            sj = j
            U.append(arr[i][j])
            f(i + 1, j + 1, 0, 1)
            U.remove(arr[i][j])

    print("#{} {}".format(tc + 1, maxV))

def get_permutation(num, cnt):
    global result, works

    if cnt > result:
        return

    if num == N:
        if result > cnt:
            result = cnt
        return

    for i in range(N):
        if not used[i]:
            used[i] = 1
            get_permutation(num + 1, cnt + works[num][i])
            used[i] = 0
    return

for tc in range(1, int(input()) + 1):
    N = int(input())
    works = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    result = 1500
    get_permutation(0, 0)
    print("#{} {}".format(tc, result))
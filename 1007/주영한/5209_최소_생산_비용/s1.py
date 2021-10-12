def get_permutation(temp = []):
    global result
    if len(temp) == N:
        temp_result = 0
        for row, col in enumerate(temp):
            temp_result += works[row][col-1]
        if result > temp_result:
            result = temp_result
        return

    for i in range(N):
        if not used[i]:
            used[i] = 1
            temp.append(i + 1)
            get_permutation(temp)
            temp.pop()
            used[i] = 0
    return

for tc in range(1, int(input()) + 1):
    N = int(input())
    works = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    result = 1500
    get_permutation()
    print("#{} {}".format(tc, result))
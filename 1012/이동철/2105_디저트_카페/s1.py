import sys
sys.stdin = open('sample_input.txt', 'r')


# 시작점과 왼쪽, 오른쪽 길이 인자로 들어오면 돌면서 카페 종류 검사
def check_desserts(dr, dc, left, right):
    global max_result
    cafe = [0] * 101
    # 카페 종류 검사용
    cnt = 0
    # 들린 카페 갯수
    lr = dr + left
    lc = dc - left
    # 왼쪽 꼭지점
    rr = dr + right
    rc = dc + right
    # 오른쪽 꼭지점
    br = dr + left + right
    bc = dc + right - left
    # 아래 꼭지점

    # 왼쪽 길이만큼 두 변 검사
    for dis in range(1, left + 1):
        if cafe[A[dr + dis][dc - dis]]:
            return
        cafe[A[dr + dis][dc - dis]] = 1
        if cafe[A[br - dis][bc + dis]]:
            return
        cafe[A[br - dis][bc + dis]] = 1
        cnt += 2

    # 오른쪽 길이만큼 두 변 검사
    for dis in range(1, right+1):
        if cafe[A[lr+dis][lc+dis]]:
            return
        cafe[A[lr+dis][lc+dis]] = 1
        if cafe[A[rr-dis][rc-dis]]:
            return
        cafe[A[rr-dis][rc-dis]] = 1
        cnt += 2

    max_result = max(max_result, cnt)
    # 최댓값 갱신


# 시작점 기준으로 좌, 우 가능한 거리 경우의 수 구하기
def make_distance(dr, dc):
    for left in range(1, dc+1):
        for right in range(1, N-dc):
            if dr + left + right > N - 1:
                # 반대편 꼭지점이 맵 넘어가면 continue
                continue
            check_desserts(dr, dc, left, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    max_result = -1
    for row in range(N-2):
        for col in range(1, N-1):
            make_distance(row, col)

    print("#{} {}".format(tc, max_result))


####################################################################################


# 다른 사람 풀이
# stack = []
# history = set([])
#
#
# def is_safe(i, j):
#     if -1 < i < M and -1 < j < M:
#         if arr[i][j] in stack:
#             return 0
#
#         if visit[i][j] == 0:
#             return 1
#     return 0
#
#
# def search(a, b, prev):
#     global max_eat
#
#     if [a, b] == start and 3 < len(stack):
#         max_eat = max(max_eat, len(stack))
#         return
#     # 방향
#     dirs = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
#
#     # 방향을 틀면 기존에 가던 방향으로는 못간다
#     for i, j in dirs:
#         if (i, j) not in history:
#             X = a + i
#             Y = b + j
#             if is_safe(X, Y):
#                 visit[X][Y] = 1
#                 stack.append(arr[X][Y])
#                 if prev != (i, j):
#                     history.add(prev)
#                     search(X, Y, (i, j))
#                     history.remove(prev)
#                 else:
#                     search(X, Y, prev)
#
#                 visit[X][Y] = 0
#                 stack.pop()
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     M = int(input())
#     arr = [list(map(int, input().split())) for _ in range(M)]
#
#     max_eat = 0
#     visit = [[0] * M for _ in range(M)]
#     # 출발점
#     for a in range(M):
#         for b in range(M):
#             start = [a, b]
#             search(a, b, (1, 1))
#
#     if max_eat == 0:
#         max_eat = -1
#
#     print('#{} {}'.format(tc, max_eat))

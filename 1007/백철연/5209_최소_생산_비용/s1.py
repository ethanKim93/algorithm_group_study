import sys
sys.stdin = open('sample_input.txt')

# def DFS(y, sum):
#     global result
#
#     if y == N:
#         if result > sum:
#             result = sum
#         return
#
#     if result < sum:
#         return
#
#     for x in range(N):
#         if not v[x]:
#             v[x] = 1
#             DFS(y+1, sum + product[y][x])
#             v[x] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     product = [list(map(int, input().split())) for _ in range(N)]
#     v = [0] * N
#     result = 100 * N**2
#
#     DFS(0, 0)

def pick(step=0, total=0):
    global minimum  # 가장 작은 값
    if minimum <= total:  # 가장 작은 값보다 지금 들고 있는 값이 크거나 같다면
        return

    if step == N:  # 마지막까지 왔을 때
        minimum = total  # 지금 들고 있는 값은 minimum보다 작을 수 밖에 없음, 위 if 참조
        return

    for i in range(N):
        if check[i]:  # 중복 체크
            check[i] = False  # 중복되지 않게끔 막음
            pick(step + 1, total + field[step][i])  # 재귀
            check[i] = True  # 해제


for case in range(int(input())):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    check = [True] * N
    minimum = 99 * N
    pick()
    print("#{} {}".format(case + 1, minimum))



# rank 사용
import sys

sys.stdin = open('s_input.txt', 'r')


def makeset(x):
    p[x] = x
    rank[x] = 0


def findset(x):  # findset 연산, x가 속한 무리의 대표를 반환
    if x != p[x]:
        p[x] = findset(p[x])
    return p[x]


def union(x, y):  # union 연산, y를 x의 무리에 묶기
    px = findset(x)
    py = findset(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # N : 사람수(1~N) M : pair 수
    p = [0] * (N+1)  # MakeSet, 마을사람 각각을 무리로 만들기
    rank = [0] * (N + 1)
    for i in range(N+1):
        makeset(i)
    for _ in range(M):
        x, y = map(int, input().split())  # 관계정보 입력 받고
        union(x, y)  # 두 사람 무리짓기

    answer = 0
    for i in range(1, N + 1):
        if i == p[i]:
            answer += 1
    print('#{} {}'.format(tc, answer))

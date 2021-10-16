import sys
sys.stdin = open("input.txt")
#5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기
def findset(x):
    if x == p[x]:
        return x
    else:
        return findset(p[x])

def union(x, y):
    if findset(x) == findset(y):
        return
    else:
        p[findset(x)] = findset(y)
        return

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    p = [_ for _ in range(N+1)]
    apps = list(map(int, input().split()))

    for i in range(M):
        x, y = apps[2*i], apps[2*i+1]
        union(x, y) # 신청서 하나씩 짝지어 줌
    for j in range(1, N+1): # root 번호로 다 바꿔줌
        if p[j] != j:
            p[j] = findset(p[i])
    print('#{} {}'.format(tc, len(set(p[1:]))))


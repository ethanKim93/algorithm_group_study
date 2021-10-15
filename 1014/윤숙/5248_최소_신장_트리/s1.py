#지영님 코드를 기반으로 쉐도우 코딩하며 이해하려 해봤습니다.
#아직개념이 잡히지 않아서 힘드네요.
import sys
sys.stdin = open('input.txt')


def find(x):
    while T[x] != x:
        x = T[x]
    return x


# 0번 인덱스에 1번이 들었는지 1번인덱스에 2번이 들었는지 확인
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    values = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        values.append([w, n1, n2])
    values.sort()
    cnt = res = 0
    T = [i for i in range(V + 1)]
    for w, n1, n2 in values:
        #유니온
        if find(n1) != find(n2):
            cnt += 1
            res += w
            #p1과 p2 합치기
            T[find(n1)] = find(n2)
        if cnt == V:
            break
    print(res)

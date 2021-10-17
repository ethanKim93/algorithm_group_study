import sys
sys.stdin = open('input.txt')


def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])


T = int(input())
for tc in range(1, T+1):
    N = int(input())                                    # 섬 개수
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())                                  # 환경 부담금 세율
    distance = []
    for i in range(N-1, -1, -1):
        target = i - 1
        while target >= 0:
            L2 = abs(x_list[i]-x_list[target])**2 + abs(y_list[i]-y_list[target])**2
            distance.append([L2, i, target])
            target -= 1
    distance.sort()

    p = [i for i in range(N + 1)]  # make_set
    cnt = 0
    total = 0  # 가중치의 합

    for L2, s, e in distance:  # N-1개의 간선 선택 루프
        if find_set(s) != find_set(e):  # 사이클을 형성하지 않으면 선택
            cnt += 1
            total += L2  # 가중치의 합
            p[find_set(e)] = find_set(s)  # v의 대표원소를 u의 대표원소로 바꿈
            if cnt == N:
                break

    ans = total * E
    print('#{} {}'.format(tc, int(ans)))




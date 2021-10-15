# 밑 코드 제출하니까 맞았는데
# 아무랑도 연결되지 않은 한 사람도 하나의 무리로 치는 코드임. 이거 되는 건지 궁금.

import sys
sys.stdin = open('s_input.txt')

def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = [i for i in range(N+1)]  # make_set
    for _ in range(M):
        for a, b in [map(int, input().split())]:
            p[find_set(b)] = find_set(a)  # union
    # 무리 수 세기
    ans = 0
    for i in range(1, N+1):
        if p[i] == i:
            ans += 1
    print('#{} {}'.format(tc, ans))

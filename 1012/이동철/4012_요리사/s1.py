import sys
sys.stdin = open('sample_input.txt', 'r')


# 재료들의 조합을 만들어서 풀면 되겠다고 생각했다.
# 먼저 식재료 수 N 을 2로 나눈 개수 만큼의 재료 조합을 구하면
# 나머지는 알아서 따라오게 되어있기에 dfs 를 N // 2 까지 탐색하도록 하였으며
# 방문배열을 통해 방문 내역이 있다면 A에 없다면 B에 집어넣었다.
# DFS 를 통해 재료의 조합을 구하고 이를 반복문을 통해 시너지 값을 구한 후
# 비교를 통해 최소값을 찾아내면 된다.


def synergy(comb):
    # 음식의 시너지값 계산 함수
    score = 0
    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            score += recipe[comb[i]][comb[j]] + recipe[comb[j]][comb[i]]
    return score


def dfs(idx, k):
    global result
    if idx == N // 2:
        # 한 음식에 선택되는 재료개수 = N // 2 이므로 재료개수만큼 탐색
        A = []
        # A 음식에 들어갈 재료
        B = []
        # B 음식에 들어갈 재료
        for j in range(N):
            # 방문 배열 개수만큼 탐색해서, 방문 내역이 있다면 A로 아니면 B에 저장
            if visit[j]:
                A.append(j)
            else:
                B.append(j)
        recipe_A = synergy(A)
        recipe_B = synergy(B)
        if abs(recipe_A - recipe_B) < result:
            result = abs(recipe_A - recipe_B)
        return

    for i in range(k, N):
        # 조합 k 인자 i까지 봤으면 다음번에는 앞에 탐색했던 부분 볼 필요 없음
        # k인자 없으면 0부터 탐색하기에 순열이 되버림
        if not visit[i]:
            visit[i] = 1
            dfs(idx + 1, i + 1)
            visit[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    recipe = [list(map(int, input().split())) for _ in range(N)]
    visit = [0 for _ in range(N)]
    result = 987654321
    dfs(0, 0)
    print('#{} {}'.format(tc, result))
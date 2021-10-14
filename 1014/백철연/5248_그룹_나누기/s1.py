import sys
sys.stdin = open('sample_input.txt')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int,input().split())
#     team = list(map(int,input().split()))
#
#     team_set = set(team)
#     d = len(team) - len(team_set) # 중복된 요소를 뺀 리스트 길이와 원래 리스트 길이와의 차를 구해보면 몇 팀이 엮여 있는지 알 수 있음
#     no_team = N - len(team_set) # 조짜기에 참여하지 않은 번호의 수, 자기 혼자 단독 팀.
#
#     if M == 0:
#         print('#{} {}'.format(tc, len(team_set))) # 전부 단독 팀일때?
#     # [9/10]
#     elif M == 1:
#         print('#{} {}'.format(tc, len(team)-1)) # 하나만 팀일 때?
#     # [9/10]
#     elif len(team) % 2 != 0:
#         print('#{} {}'.format(tc, len(team) // 2 - d + no_team + 1)) # 팀이 홀수 일때?
#     # [9/10]
#
#
#     print('#{} {}'.format(tc, len(team) // 2 - d + no_team))
#     # [9/10]


# 장지빈
def find(V):
    for i in range(1, N+1):
        if not visited[i] and adj[V][i]:
            visited[i] = 1
            find(i)
    return
for tc in range(1, int(input())+1):
    ans = 0
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    adj = [[0]*(N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    for i in range(M):
        a, b = li[i*2], li[(i*2)+1]
        adj[a][b] = 1
        adj[b][a] = 1
    # pprint(adj)
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            find(i)
            ans += 1
    print('#{} {}'.format(tc, ans))
import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    T, N = map(int,input().split())
    citys = list(map(int, input().split()))

    #인접행렬정의
    adj = [[0]*100 for _ in range(100)]

    # 2개씩 돌며 간선위치 저장
    for i in range(0, len(citys), 2):
        adj[citys[i]] += [citys[i+1]]

    visited = [0]*100 #방문한거 저장할 곳
    stack = [0] #미리 하나 너놓기.. 뭘..?
    while stack:
        j = stack.pop() #아무것도 조건에 해당되지 않으면
        if not visited[j]:
            visited[j] = 1
            for i in range(len(adj[j])):
                if not visited[adj[j][i]]:
                    stack.append(adj[j][i])

    print('#{} {}'.format(tc, visited[-1]))
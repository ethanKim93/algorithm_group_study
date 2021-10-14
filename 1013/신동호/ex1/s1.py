# 7
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
N = int(input())
E = list(map(int, input().split()))
s = [0] * (N+1)
visited = [0] * (N+1)

top = -1
def push_s(s, v):
    global top
    top += 1
    s[top] = v

def pop_s(s):
    global top
    top -= 1
    return s[top+1]

def DFS(V):
    global s, top
    push_s(s, V)
    while not top == -1:
        v = pop_s(s)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in link[v]:
                if not visited[w]:
                    push_s(s, w)


link = [[] for _ in range(N+1)]
for i in range(0, len(E), 2):
    link[E[i]].append(E[i+1])
    link[E[i+1]].append(E[i])
DFS(1)

# 인접 리스트
# adjL = [[0] * (N+1) for _ in range(N+1)]
# for i in range(0, len(E), 2):
#     adjL[E[i]][E[i+1]] = 1
#     adjL[E[i+1]][E[i]] = 1

# print(adjL)
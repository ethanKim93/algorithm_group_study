import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())        #노드/간선
    matrix = [[] for _ in range(V+1)]       #0번부터V번째까지 리스트 / 확인용
    for _ in range(E):  #간선 개수만큼
        start, end = map(int, input().split())
        matrix[start].append(end)       #시작과 끝을 표시
    S, G = map(int, input().split())

    visited = [0] * (V+1)         #방문여부 확인 리스트

    stack = [S]     # 아래 조건문을 돌리기 위해 일단 S 넣어놓고 시작 start
    while stack:        #스택이 다 비워질 때 까지 반복을 돌거야
        vertex = stack.pop()
        if not visited[vertex]:     #0이라면
            visited[vertex] = 1     #1 넣어주며 방문 체크
            for v in matrix[vertex]:
                if not visited[v]: #v번째에 간 적이 없으면
                    stack.append(v) #stack에 v 추가

    result = 1 if visited[G] else 0       #도착점G번 방문했는지 확인
    print('#{} {}'.format(tc, result))
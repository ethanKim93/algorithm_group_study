import sys
sys.stdin = open("sample_input.txt")

def tracking(table, V, visited, start, target):
    # 반복문을 통해 해당 start 노드에서 갈 수 있는 노드들을 확인한다.
    for i in range(V):
        move = table[start][i]
        if move and not visited[i]:
        # 방문하지 않았고, 갈 수 있다면 아래를 확인한다.
            if i == target:
                # 목표 노드에 도착하면 1을 반환한다.
                return 1
            else:
                # 목표 노드가 아니라면 일단 방문한 뒤, 재귀적으로 함수를 불러낸다.
                # 이때 재귀적으로 불러낸 함수에 인자로 i(방문한 노드)를 넣어준다.
                visited[i] = 1
                if tracking(table, V, visited, i, target):
                    return 1
                # 목표 노드를 찾는 경우(1이 반환 될 경우) 재귀적으로 1을 반납한다.

        else :
            # 길이 막혔거나 더 방문할 이유가 없다면 다른 노드를 확인해본다.
            continue
    # 모든 노드를 확인했을 때 목표 노드에 가지 못하면 0을 반환한다.
    return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 연결 상태에 대한 테이블 connection 생성
    connection = [[0] * V for _ in range(V)]
    for _ in range(E):

        # 노드 번호와 인덱스의 범위를 통일시키기 위해서 1을 뺴준다.
        row, col = map(lambda x : int(x) - 1, input().split())
        connection[row][col] = 1

    S, G = map(lambda x : int(x) - 1, input().split())
    visited = [0] * V
    visited[S] = 1

    print("#{} {}".format(tc, tracking(connection, V, visited, S, G)))
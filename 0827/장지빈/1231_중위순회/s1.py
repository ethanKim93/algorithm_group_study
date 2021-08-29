import sys
sys.stdin =open('input.txt')


def order(n):      #중위
    if len(edge[n]) == 4:
        order(int(edge[n][2]))  # n의 왼쪽 자식이 있는지 없는지 확인 / 없을때까지
        print(edge[n][1], end='')  # 방문할 자식이 었으면 리턴되고 본인 출력
        order(int(edge[n][3]))  # 올라가며 부모노드 반환
    elif len(edge[n]) == 3:
        order(int(edge[n][2]))  # n의 왼쪽 자식이 있는지 없는지 확인 / 없을때까지
        print(edge[n][1], end='')  # 방문할 자식이 었으면 리턴되고 본인 출력
    else:
        print(edge[n][1], end='')


for tc in range(1, 11):
    V = int(input())
    edge = [input().split() for _ in range(V)]
    edge = [[0]] + edge
    print('#{}'.format(tc), end=' ')
    order(1)
    print()

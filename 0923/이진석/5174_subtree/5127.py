import sys
sys.stdin = open('sample_input.txt')


def pre_order(n):
    global cnt
    if n:
        cnt += 1
        pre_order(left[n])
        pre_order(right[n])

for tc in range(1, int(input()) + 1):
    E, N = map(int, input().split())    # E : 간선의 갯수 N : 타겟 노드
    edge = list(map(int, input().split()))  # 부모-자식 노드 번호 쌍
    left = [0] * (E + 2)    # 노드가 E+1번까지 존재하기 때문에 E+1번 인덱스까지
    right = [0] * (E + 2)
    for i in range(E):
        p, c = edge[i * 2], edge[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    cnt = 0
    pre_order(N)
    print('#{} {}'.format(tc, cnt))
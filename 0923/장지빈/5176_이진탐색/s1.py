import sys
sys.stdin = open('input.txt')


def in_order(v):  # 중위순회
    global num
    if v < N+1:  # 트리의 범위 안 인덱스에러 방지
        in_order(2*v)  # 왼쪽 확인
        tree[v] = num
        num += 1  # 1부터 1씩 더해준다.
        in_order(2*v+1)  # 오른쪽 확인


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)  # 값이 0, 노드수가 N인 완전이진트리 생성
    num = 1
    in_order(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))

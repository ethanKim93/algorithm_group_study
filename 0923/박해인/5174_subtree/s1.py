import sys
sys.stdin = open('sample_input.txt')

def in_order(n):  # 중위순회
    global cnt
    if n:
        in_order(left[n])
        cnt += 1
        in_order(right[n])

T = int(input())
for test_case in range(1, T+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))

    # 이진트리
    left = [0] * (E+2)  # 정점의 총 수 + 1 = 간선의 수 + 2
    right = [0] * (E+2)

    for i in range(0, len(data), 2):
        parents, child = data[i], data[i+1]
        if not left[parents]:  # 왼쪽 자식이 없으면 왼쪽 자식
            left[parents] = child
        else:  # 왼쪽 자식이 있으면 오른쪽 자식
            right[parents] = child

    cnt = 0
    in_order(N)
    print('#{} {}'.format(test_case, cnt))
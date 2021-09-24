import sys
sys.stdin = open('sample_input.txt')

# 순회하면서 하나씩 세주기
def inorder(node):
    global cnt
    if node == 0:
        return
    cnt += 1
    inorder(left[node])
    inorder(right[node])


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    left = [0] * (E+2)  # 범위 E+2 만큼 빈 리스트
    right = [0] * (E+2)

    # 쌍으로 주어지니까 범위 2씩
    for i in range(0, len(arr),2):
        p, c = arr[i], arr[i+1]
        # 이미 왼쪽 있으면 오른쪽으로 가고
        if left[p]:
            right[p] = c
        # 나머지는 왼쪽부터 채우기
        else:
            left[p] = c

    cnt = 0
    inorder(N)
    print('#{} {}'.format(tc, cnt))

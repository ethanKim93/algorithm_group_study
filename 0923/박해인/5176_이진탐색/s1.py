import sys
sys.stdin = open('sample_input.txt')

def inorder(n):
    global value
    if n <= N:
        inorder(n*2)  # 왼쪽 자식
        tree[n] = value
        value += 1
        inorder(n*2+1)  # 오른쪽 자식

# 루트에 저장된 값, N//2에 저장된 값 출력
T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    tree = [0 for _ in range(N+1)]

    value = 1
    inorder(1)  # 무조건 루트를 1번으로 하는 이진 트리
    print('#{} {} {}'.format(test_case, tree[1], tree[N//2]))
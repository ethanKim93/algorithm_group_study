import sys
sys.stdin = open('input.txt')

operator = ['+', '-', '*', '/']

def calculator(n):
    if left[n]:
        if tree[n] == '+':
            return calculator(left[n]) + calculator(right[n])
        elif tree[n] == '-':
            return calculator(left[n]) - calculator(right[n])
        elif tree[n] == '*':
            return calculator(left[n]) * calculator(right[n])
        elif tree[n] == '/':
            return calculator(left[n]) / calculator(right[n])
    else:
        return tree[n]
T = 10
for test_case in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for _ in range(N):
        data = list(input().split())
        if data[1] in operator:  # 정점이 연산자이면,
            left[int(data[0])] = int(data[2])  # 해당 정점의 왼쪽 자식
            right[int(data[0])] = int(data[3])  # 해당 정점의 오른쪽 자식
            tree[int(data[0])] = data[1]  # 트리에 연산자를 넣는다.
        else:  # 정점이 단순한 수이면,
            tree[int(data[0])] = int(data[1])  # 트리에 값을 넣는다.

    print('#{} {}'.format(test_case, int(calculator(1))))
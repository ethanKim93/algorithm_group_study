import sys
sys.stdin = open('input.txt')

def in_order(n):
    if n:
        in_order(left[n])
        print(tree[n], end='')
        in_order(right[n])

for test_case in range(1):
    N = int(input())  # 정점의 총 수
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(1, N+1):
        data = list(input().split())
        tree[int(data[0])] = data[1]
        if len(data[2:]) == 2:
            left[int(data[0])] = int(data[2])
            right[int(data[0])] = int(data[3])
        elif len(data[2:]) == 1:
            left[int(data[0])] = int(data[2])

    print('#{} '.format(test_case), end='')
    in_order(1)
    print()
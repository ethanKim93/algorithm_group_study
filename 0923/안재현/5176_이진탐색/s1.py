import sys
sys.stdin = open('sample_input.txt')


def tree(node, value):
    if node > N:
        return value
    else:
        value = tree(node * 2, value)
        value += 1
        arr[node] = value
        value = tree(node * 2 + 1, value)
        return value


T = int(input())

for tc in range(0, T):
    N = int(input())
    arr = [0] * (N + 1)
    print(arr)
    tree(1, 0)
    print(arr)
    print('#{} {} {}'.format(tc + 1, arr[1], arr[N//2]))
import sys
sys.stdin = open('sample_input.txt')

def heap(number):
    for i in range(1, N + 2):
        if tree[i] == 0:
            tree[i] = number
            break
    while not (tree[i] > tree[i//2]):
        tree[i], tree[i//2] = tree[i//2], tree[i]
        i //= 2

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    tree = [0] * (N + 1)

    for i in range(len(numbers)):
        num = numbers[i]
        heap(num)

    idx = len(tree) - 1
    result = -tree[idx]
    while idx > 0:
        result += tree[idx]
        idx //= 2
    print("#{} {}".format(tc, result))
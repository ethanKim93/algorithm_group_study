import sys
sys.stdin = open('sample_input.txt')


def tree(n):
    global cnt
    if n == 0:
        return
    cnt += 1
    tree(left[n])
    tree(right[n])


T = int(input())

for tc in range(0, T):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for i in range(0, len(arr), 2):
        r1, r2 = arr[i], arr[i + 1]
        if left[r1]:
            right[r1] = r2
        else:
            left[r1] = r2
    cnt = 0
    tree(N)
    print('#{} {}'.format(tc + 1, cnt))
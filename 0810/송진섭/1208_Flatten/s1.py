import sys
sys.stdin = open('input.txt')


def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


for tc in range(1, 11):
    dump = int(input())
    brick = list(map(int, input().split()))

    brick = bubble_sort(brick)
    for i in range(dump):
        brick[99] -= 1
        brick[0] += 1
        brick = bubble_sort(brick)
    answer = brick[99] - brick[0]
    print('#{} {}'.format(tc, answer))


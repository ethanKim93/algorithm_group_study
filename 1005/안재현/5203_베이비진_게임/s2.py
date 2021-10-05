import sys
sys.stdin = open('sample_input.txt')


def check_run_triplet(arr):
    arr.sort()
    for j in range(len(arr) - 2):
        if arr[j] + 2 == arr[j + 1] + 1 == arr[j + 2] or arr[j] == arr[j + 1] == arr[j + 2]:
            return True
    return False

T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    winner = 0
    p1 = []
    p2 = []
    for i in range(0, len(numbers), 2):
        p1.append(numbers[i])
        p2.append(numbers[i + 1])
        if check_run_triplet(p1):
            winner = 1
            break
        if check_run_triplet(p2):
            winner = 2
            break

    print('#{} {}'.format(tc, winner))


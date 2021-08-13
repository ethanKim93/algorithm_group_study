import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 버블정렬
    for end in range(N-1, 0, -1):
        for i in range(0, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    print('#{} {}'.format(tc, ' '.join(map(str, arr))))
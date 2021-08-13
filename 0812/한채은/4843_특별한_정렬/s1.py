import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(10):
        minmax = i      # minmax값만 바꾸는 형태로
        for j in range(i + 1, N):
            if i % 2:
                if arr[minmax] > arr[j]:
                    minmax = j
            else:
                if arr[minmax] < arr[j]:
                    minmax = j
        arr[i], arr[minmax] = arr[minmax], arr[i]

    print('#{} {}'.format(tc, ' '.join(map(str,arr[:10]))))
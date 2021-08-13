import sys
sys.stdin=open('sample_input.txt')


def selection_sort(a, n):   # 선택정렬
    for i in range(n-1):
        min_idx = i
        for j in range(i, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    sa = selection_sort(a, N)   # 주어진 배열을 정렬

    result = []
    for i in range(1, N+1):     # 큰 수와 작은 수가 번갈아 나오는 result 생성
        if i % 2:
            result += [sa[-(i//2+1)]]
        else:
            result += [sa[i//2-1]]

    print('#{} '.format(tc), end='')
    print(*result[:10], sep=' ')
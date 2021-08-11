import sys
sys.stdin = open("input.txt")
# counting sort 구현
def counting_sort(a):
    sort_a = [0]*len(a)
    min_n = max_n = a[0]
    for _ in a:
        if _ > max_n:
            max_n = _
        if _ < min_n:
            min_n = _
    cnt = [0] * (max_n - min_n + 1)

    for idx in map(lambda x: x-min_n, a):
        cnt[idx] += 1

    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]

    for i in range(len(a)-1, -1, -1):
        cnt[a[i]-min_n] -= 1
        sort_a[cnt[a[i]-min_n]] += a[i]

    return sort_a

for tc in range(1, 11):
    dump = int(input())
    boxs = list(map(int, input().split()))

    while (dump > 0):
        boxs = counting_sort(boxs)
        boxs[0] += 1
        boxs[-1] -= 1
        dump -= 1
        height = counting_sort(boxs)
        if height[-1]-height[0] <= 1:
            break

    print('#{} {}'.format(tc, height[-1]-height[0]))





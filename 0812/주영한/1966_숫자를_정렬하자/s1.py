import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_lists = list(map(int, input().split()))

    # 선택정렬 수행
    for i in range(N):
        min_idx = i
        min_value = num_lists[min_idx]
        for j in range(i, N):
            if min_value > num_lists[j]:
                min_idx = j
                min_value = num_lists[j]
        num_lists[i], num_lists[min_idx] = num_lists[min_idx], num_lists[i]

    print("#{} {}".format(tc, " ".join(map(str, num_lists))))
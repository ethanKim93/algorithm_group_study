import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    main_str, cmp_str = input().split()
    M, C = len(main_str), len(cmp_str)
    cnt = 0
    start_idx = 0
    while start_idx < M:
        if main_str[start_idx:start_idx+C] == cmp_str:
            start_idx = start_idx + C
        else:
            start_idx += 1
        cnt += 1
    print("#{} {}".format(tc, cnt))
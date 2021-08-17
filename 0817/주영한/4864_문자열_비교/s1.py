import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    cmp_str = input()
    main_str = input()
    C, M = len(cmp_str), len(main_str)
    result = 0
    for i in range(M - C + 1):
        for j in range(C):
            if main_str[i + j] != cmp_str[j]:
                break
            if j == C - 1:
                result = 1
        if result:
            break

    print('#{} {}'.format(tc, result))
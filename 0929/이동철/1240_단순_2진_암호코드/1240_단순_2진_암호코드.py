import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N = 세로, M = 가로
    arr = [list(input()) for _ in range(N)]

    secret = [
        '0001101', '0011001', '0010011', '0111101', '0100011',
        '0110001', '0101111', '0111011', '0110111', '0001011'
    ]

    code = ''
    for i in range(N):
        if '1' in arr[i]:
            for j in range(M):
                code += arr[i][j]
            break
    # print(code)

    reverse_code = code[::-1]
    for i in range(M):
        if reverse_code[i] == '1':
            reverse_code = reverse_code[i:i+56]
            break
    # print(reverse_code)

    code = reverse_code[::-1]
    # print(code)

    split_code = []
    for i in range(0, len(code), 7):
        split_code.append(code[i:i+7])
    # print(split_code)

    for i in range(len(split_code)):
        split_code[i] = secret.index(split_code[i])
    # print(split_code)

    sum_odd = 0
    sum_even = 0
    for i in range(len(split_code) - 1):
        if i % 2 == 0:
            sum_odd += split_code[i]
        else:
            sum_even += split_code[i]
    result = (sum_odd * 3) + sum_even + split_code[7]
    # print(sum_odd)
    # print(sum_even)
    # print(result)

    if result % 10 == 0:
        print('#{} {}'.format(tc, sum(split_code)))
    else:
        print('#{} {}'.format(tc, 0))
    print()
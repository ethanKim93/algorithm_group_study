import sys
sys.stdin = open("sample_input.txt")

decode = {'112': 0, '122': 1, '221': 2, '114': 3, '231': 4,
          '132': 5, '411': 6, '213': 7, '312': 8, '211': 9}
hextobin = {'0': '0000', '1': '0001', '2': '0010',
            '3': '0011', '4': '0100', '5': '0101',
            '6': '0110', '7': '0111', '8': '1000', '9': '1001',
            'A': '1010', 'B': '1011', 'C': '1100',
            'D': '1101', 'E': '1110', 'F': '1111'}


def check(arr):
    if ((arr[0] + arr[2] + arr[4] + arr[6]) * 3 + arr[1] + arr[3] + arr[5] + arr[7]) % 10:
        return False
    return True


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]

    Bin_code = [''] * N
    for i in range(N):
        for j in range(M):
            Bin_code[i] += hextobin[lst[i][j]]

    result = []
    visited = []
    answer = 0
    for i in range(N):
        a = b = c = 0
        for j in range((M * 4) - 1, -1, -1):
            if b == 0 and c == 0 and Bin_code[i][j] == '1':
                a += 1
            elif a > 0 and c == 0 and Bin_code[i][j] == '0':
                b += 1
            elif a > 0 and b > 0 and Bin_code[i][j] == '1':
                c += 1
            if a and b and c and Bin_code[i][j] == '0':
                minP = min(a, b, c)
                a = a // minP
                b = b // minP
                c = c // minP
                pattern = decode[str(a) + str(b) + str(c)]
                result.append(pattern)
                a = b = c = 0

            if len(result) == 8:
                temp = result[::-1]
                if check(temp) and temp not in visited:
                    answer += sum(result)
                visited.append(temp)
                result = []
    print('#{} {}'.format(tc, answer))
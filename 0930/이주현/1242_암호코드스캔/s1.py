import sys
sys.stdin = open('input.txt')

hex_code = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
pattern = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}

def get_number(rate):
    tmp = min(rate)
    rate[1] //= tmp
    rate[2] //= tmp
    rate[3] //= tmp
    key = str(rate[1]) + str(rate[2]) + str(rate[3])
    return pattern[key]

def get_code(binary):
    result = []
    i = len(binary) - 1
    while i > 0:
        if binary[i] == '1':
            tmp, i = translate(binary, i)
            result.append(tmp)
        else:
            i -= 1
    return result

def translate(binary, idx):
    rate = [1, 1, 1, 1]
    rate_idx = 3
    result = []
    while True:
        if rate_idx != 0:
            if binary[idx] == binary[idx - 1]:
                rate[rate_idx] += 1
            else:
                rate_idx -= 1
            idx -= 1
        else:
            rate[0] = 7*min(rate[1:]) - sum(rate[1:])
            idx -= rate[0]
            result.append(str(get_number(rate)))
            rate = [1, 1, 1, 1]
            rate_idx = 3
            if len(result) > 7:
                break
    return ''.join(result[::-1]), idx

T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    results = set()
    matrixs = sorted(list(set([input() for _ in range(N)])))[1:]
    for i in range(len(matrixs)):
        matrix = matrixs[i]
        binary = ''
        for j in range(len(matrix)):
            binary += hex_code[matrix[j]]
        tmps = get_code(binary)
        for tmp in tmps:
            results.add(tmp)

    tmp = 0
    for result in results:
        summary = (int(result[0]) + int(result[2]) + int(result[4]) + int(result[6])) * 3 + int(result[1]) + int(result[3]) + int(result[5])
        if (summary + int(result[7])) % 10 == 0:
            for i in range(len(result)):
                tmp += int(result[i])

    print("#{} {}".format(tc, tmp))
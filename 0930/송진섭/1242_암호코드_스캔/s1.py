import sys
sys.stdin = open('sample_input.txt')

code = [
    [1, 1, 2], [1, 2, 2],
    [2, 2, 1], [1, 1, 4],
    [2, 3, 2], [1, 3, 2],
    [4, 1, 1], [2, 1, 3],
    [3, 1, 2], [2, 1, 1]
    ]

hex_dict = {
    '0': '0000', '1': '0001',
    '2': '0010', '3': '0011',
    '4': '0100', '5': '0101',
    '6': '0110', '7': '0111',
    '8': '1000', '9': '1001',
    'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101',
    'E': '1110', 'F': '1111',
}

def Bbit_print(i):
    output = ''
    for j in range(3, -1, -1):                      # N자리
        output += '1' if i & (1 << j) else '0'      # i의 j자리 비트가 1인지 확인
    return output


def hex_to_bin(a_str):                                        # 거꾸로 문자를 받아 탐색하며 0으로 시작하지 않는 시작점을 찾는 함수
    binary_str = ''
    for j in range(0, len(a_str)):
        j = int(a_str[j], 16)
        binary_str += Bbit_print(j)
    return binary_str


def calculation_ratio(a, b, c):
    min_num = min(a, b, c)
    a //= min_num
    b //= min_num
    c //= min_num
    return [a, b, c]


"""
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code_problem = [list(input().split()) for _ in range(N)]

    for i in range(N):                                         # 행 탐색
        code_binary = hex_to_bin(code_problem[i][0])

        code_binary_reverse = code_binary[::-1]
        for j in range(len(code_binary_reverse)):
            if code_binary_reverse[j] == '1':
                start_point = j
                break
            elif j > len(code_binary_reverse)/8:
                start_point = -1
                break
        if start_point == -1:
            continue

        code_ratio = []
        cnt = 0
        for j in range(1, len(code_binary)):
            if code_binary_reverse[j] == code_binary_reverse[j-1]:
                cnt += 1
            else:
                code_ratio.append(cnt+1)
                cnt = 0
        code_ratio = [code_ratio[k:k + 3] for k in range(0, len(code_ratio), 4)]
        res = []
        for l in range(len(code_ratio)):
            res.append(code.index(calculation_ratio(code_ratio[l][0], code_ratio[l][1], code_ratio[l][2])))
        odd_num = res[7]+res[5]+res[3]+res[1]
        even_num = res[6]+res[4]+res[2]+res[0]
        if not ((odd_num*3)+even_num) % 10:
            print('#{} {}'.format(tc, odd_num+even_num))
            break

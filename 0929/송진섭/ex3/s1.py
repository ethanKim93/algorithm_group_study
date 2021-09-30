"""
0DEC
0269FAC9A0
"""

code = {
    '001101': 0, '010011': 1,
    '111011': 2, '110001': 3,
    '100011': 4, '110111': 5,
    '001011': 6, '111101': 7,
    '011001': 8, '101111': 9
    }


def Bbit_print(i):
    output = ''
    for j in range(3, -1, -1):
        output += '1' if i & (1 << j) else '0'
    return output


def search_start(a_str):
    for j in range(0, len(a_str)):
        if a_str[j] == '1':
            for code_pattern in code.keys():
                if code_pattern[::-1] == a_str[j:j + 6]:
                    point = j
                    return point
    return -1


def analysis_code(point):
    if point == -1:
        return None
    ans = []
    for k in range(start_point, len(bit_num_reverse), 6):
        ans.append(code.get(bit_num_reverse[k:k + 6][::-1]))
    return ans


hex_list = list(input())
bit_num = ''

for i in hex_list:
    i = int('0x'+i, 16)
    bit_num += Bbit_print(i)

bit_num_reverse = bit_num[::-1]

start_point = search_start(bit_num_reverse)

answer = analysis_code(start_point)
if len(bit_num) % 6:
    del answer[-1]

print(', '.join(map(str, answer[::-1])))



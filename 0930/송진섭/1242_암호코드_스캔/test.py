
code = {
    (1, 1, 2): 0, (1, 2, 2): 1,                                 # 검증코드를 거꾸로 저장
    (2, 2, 1): 2, (1, 1, 4): 3,
    (2, 3, 2): 4, (1, 3, 2): 5,
    (4, 1, 1): 6, (2, 1, 3): 7,
    (3, 1, 2): 8, (2, 1, 1): 9
}

code2 = [
    [1, 1, 2], [1, 2, 2],
    [2, 2, 1], [1, 1, 4],
    [2, 3, 2], [1, 3, 2],
    [4, 1, 1], [2, 1, 3],
    [3, 1, 2], [2, 1, 1]
    ]

# a = [['1', '0', '1']]
# ss = ''
# for i in range(len(a[0])):
#     ss += (a[0][i]*2)
# print(ss)
# print(code.get((2, 2, 1)))
# bi = []
# a = '0111011'
# b = '0110001011101101100010110001000110100100110111011'
# cnt = 0
# for i in range(1, 7):
#     if a[i] == a[i-1]:
#         cnt += 1
#     else:
#         bi.append(cnt+1)
#         cnt = 0
# print(bi)
# plus_ten = lambda x: x + 10
# a = map(lambda x: x ** 2, (2, 4, 6))
# print(a)

"""
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
"""
def Bbit_print(i):
    output = ''
    for j in range(3, -1, -1):                      # 4자리
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
code_binary = hex_to_bin('000000001DB176C588D26EC000')
code_binary_reverse = code_binary[::-1]
for i in range(len(code_binary_reverse)):
    if code_binary_reverse[i] == '1':
        start_point = i
        break
code_binary_reverse = code_binary_reverse[start_point::]
print(code_binary_reverse)

code_ratio = []
cnt = 0
for j in range(1, len(code_binary_reverse)):
    if code_binary_reverse[j] == code_binary_reverse[j - 1]:
        cnt += 1
    else:
        code_ratio.append(cnt + 1)
        cnt = 0
# print(code_binary_reverse)
print(code_ratio)
new_ratio = [code_ratio[k:k+3] for k in range(0, len(code_ratio), 4)]
print(new_ratio)
res = []

for l in range(len(new_ratio)):
    res.append(code2.index(calculation_ratio(new_ratio[l][0], new_ratio[l][1], new_ratio[l][2])))
print(res)

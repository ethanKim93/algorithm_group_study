crypto_patterns = [
    '001101',
    '010011',
    '111011',
    '110001',
    '100011',
    '001011',
    '111101',
    '011001',
    '101111',
]

# 16진수를 표현하는 딕셔너리 정의
hexa = {}
for idx, i in enumerate('0123456789ABCDEF'):
    hexa[i] = idx

# arr = '0DEC'
arr = '0269FAC9A0'

# 16진수 한자리는 4자리의 2진수로 표현
# 16진수를 2진수로 변환
binary = ''
for a in arr:
    for i in range(3,-1,-1):
        binary += '1' if hexa[a] & (1<<i) else '0'


# 뒤부터 찾기
length = len(binary)
i = 0
ans = []
while length>5:
    try:
        a = crypto_patterns.index(binary[length-6:length])
        ans.append(a)
        length -= 6
    except:
        length -= 1

print(*ans[::-1])
# 0F97A3
# 01D06079861D79F99F

def function(inputNum, bit):
    result = 0
    for i in range(0, bit):
        result += 2 ** (bit -1 - i) * int(inputNum[0:bit][i])
    return result


dict16 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
          '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

exp1 = '0F97A3'
num = ''

for i in exp1:
    num += dict16[i]

ans = []

# 중복 코드를 함수로 만들었다
while len(num) >= 7:
    ans.append(function(num, 7))
    num = num[7:]

if len(num) > 0:
    ans.append(function(num, len(num)))


# 처음에 쓴 코드. 중복 코드가 있다
# while len(num) >= 7:
#     num10 = 0
#     for i in range(0, 7):
#         num10 += 2**(6-i) * int(num[0:7][i])
#     ans.append(num10)
#     num = num[7:]
#
# if len(num) > 0:
#     num102 = 0
#     for i in range(0, len(num)):
#         num102 += 2**(len(num)-1-i) * int(num[i])
#     ans.append(num102)

print(ans)
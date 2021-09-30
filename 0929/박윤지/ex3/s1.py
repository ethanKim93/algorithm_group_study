inputN = '0DEC'
# inputN = '0269FAC9A0'

# 암호 딕셔너리
password = {'0': '001101',
            '1': '010011',
            '2': '111011',
            '3': '110001',
            '4': '100011',
            '5': '110111',
            '6': '001011',
            '7': '111101',
            '8': '011001',
            '9': '101111'}

# 위 딕셔너리의 key, value 반대로
password_r = {v:k for k,v in password.items()}

# 16진수 한 글자에 대응하는 2진수
dict16 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
          '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}


num = ''

# 입력값을 2진수로 만들기
for i in inputN:
    num += dict16[i]

# 2진수의 뒤에서부터 탐색하여 암호비트패턴이 끝나는 지점 찾기
end = 0
for j in range(len(num)-1, -1, -1):
    if num[j] == '1':
        if num[j-5:j+1] in password.values():
            end = j
            break

# 암호 출력할 리스트
ans = []

try:
    while end > 4:
        ans = [password_r[num[end-5:end+1]]] + ans
        end -= 6
except:
    print(ans)

print(ans)
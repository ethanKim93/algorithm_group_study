text = '0000000111100000011000000111100110000110000111100111100111111001100111'
answer = []

for i in range(0,len(text),7):
    # answer.append(int('0b' + text[i:i+7],2))  2진수를 10진수로 변환
    num = text[i:i+7]
    temp = 0
    for j in range(7):
        temp += (2 ** (7-j-1)) if num[j]=='1' else 0
    answer.append(temp)

print(answer)
# 16진수를 표현하는 딕셔너리 정의
hexa = {}
for idx, i in enumerate('0123456789ABCDEF'):
    hexa[i] = idx

# 16진수 문자로 이루어진 1차 배열
# arr = '0F97A3'
arr = '01D06079861D79F99F'

# 16진수 한자리는 4자리의 2진수로 표현
# 16진수를 2진수로 변환
binary = ''
for a in arr:
    for i in range(3,-1,-1):
        binary += '1' if hexa[a] & (1<<i) else '0'

print(binary, len(binary))
    
# 앞에서 부터 7bit씩 묶어 십진수로 변환
ans = []
for i in range(0, len(binary), 7):
    # 7보다 작을 경우 앞을 0 으로 보충해줌
    if i+7 > len(binary):
        bins = [0]*(7-(len(binary)-i)) + list(map(int,binary[i:]))
    else:
        bins = list(map(int,binary[i:i+7]))

    dec = 0
    for j in range(7):
        dec += 1<<j if bins[6-j] & 1 else 0
    ans.append(dec)

print(*ans)
bit = list(map(int,'0000000111100000011000000111100110000110000111100111100111111001100111'))

# 7개 byte를 묶어서 10진수로 출력하기
ans = []
for i in range(0, len(bit),7):
    dec = 0
    for j in range(7):
        # 7자리의 첫째자리부터 1이면, 해당 자리의 2진수 값을 누적
        if bit[i+7-j-1] & 1:
            dec += 1<<j
    ans.append(dec)

print(*ans)


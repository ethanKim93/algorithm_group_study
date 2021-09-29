bt = '0000000111100000011000000111100110000110000111100111100111111001100111'

bts = []
ans = []
for i in range(0,len(bt),7):
    bts.append(bt[i:i+7])
for j in bts:
    ans.append(int(j, 2))
print('int 함수 할용 : {}'.format(ans))

tots = []
for b in bts:
    tot = 0
    for idx in range(1,8):
        if b[-idx] == '1':
            tot += (2**(idx-1))
    tots.append(tot)
print('반복문 활용 : {}'.format(tots))
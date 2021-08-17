strs = 'Hell come to Algorithm Course'
n = len(strs)
# 임시 빈 리스트 만들기
strs_rev = [0]*n
for i in range(n//2):
    # strs_rev[n-1-i], strs_rev[i] = strs[i], strs[n-1-i]
    temp = strs[i], strs[n-1-i]
    strs_rev[n-1-i], strs_rev[i] = temp

print('Origin: {}'.format(strs))
print('Flipped: {}'.format(''.join(map(str, strs_rev))))






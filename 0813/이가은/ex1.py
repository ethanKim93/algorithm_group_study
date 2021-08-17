S = 'Reverse this strings'

# slicing index 이용
sli_reverse = S[::-1]
print(sli_reverse)


revers_str = []
for i in range(len(S)):
    revers_str.append(S[len(S)-1-i])
print(''.join(revers_str))
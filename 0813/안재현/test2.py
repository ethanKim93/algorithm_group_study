cnt = [0]*26
s = 'aba'
print(ord('a'))
for x in s:
    if 'a' <= x <= 'z':
        cnt[ord(x)-ord('a')] += 1
    elif 'A' <= x <= 'Z':
        print(x)
    elif '0' <= x < '9':
        print('숫자')

print(cnt)
print(chr(65))
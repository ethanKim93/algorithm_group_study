word = input()
cnt = len(word)

# 자기 문자열에서 뒤집는 방법
if cnt % 2:
    for i in range(cnt // 2):
        word[i], word[cnt - 1 - i] = word[cnt - 1 - i], word[i]
else:
    for i in range(cnt // 2 - 1):
        word[i], word[cnt - 1 - i] = word[cnt - 1 - i], word[i]

# 빈 문자열을 만들어 소스의 뒤에서부터 읽어서 타겟에 쓰는 방법
reverse = ''
for i in range(cnt - 1, -1, -1):
    reverse += word[i]

# reverse 함수 혹은 slice notation 을 이용하여 구현
print(''.join(reversed(word)))
word = word[::-1]
print(word)

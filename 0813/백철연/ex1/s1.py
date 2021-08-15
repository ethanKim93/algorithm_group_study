s = list(input())
n = len(s) # 글자수
tem = ''
for i in range(n//2):
    tem = s[i]
    s[i] = s[n-1-i]
    s[n-1-i] = tem

print(s)

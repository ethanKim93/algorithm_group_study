s = list(input())
n = len(s) # κΈμμ
tem = ''
for i in range(n//2):
    tem = s[i]
    s[i] = s[n-1-i]
    s[n-1-i] = tem

print(s)

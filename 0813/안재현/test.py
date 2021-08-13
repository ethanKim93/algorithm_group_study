s1 = 'a b a'
s2 = s1.replace('a', 'd')
s3 = s1.split()  # 빈 칸을 기준으로 자른다.
s4, s5, s6 = s1.split()
s7 = 'aba'
print(s1)
print(s2)
print(s3)
print(s4, s5, s6)
print(s1.isalpha())  # 빈칸없이 모두 소문자일때만 True 이외에는 False
print(s7.isalpha())

s8 = 'ab A'
print(s1[0])
# s1[0] = 'B' # str' object does not support item assignment str은 리스트가 아니므로 특정 위치를 기준으로 변경은 안된다.

s = list(input())
n = len(s)
for i in range(n//2):
    s[i], s[n-1-1] = s[n-1-i], s[i]
print(s)

# s = [::-1] # 이런 식으로 하면 앞뒤가 바뀐다
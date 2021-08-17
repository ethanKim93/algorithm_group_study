s = input()
s3 = s2 = s
# 1
print(s[::-1])

# 2
print("".join(reversed(s)))

# 3
ans = ""
for i in reversed(s):
    ans += (i)

print(ans)

# 4
s = list(s)
for i in range(len(s)//2):
    s[i], s[-i-1] = s[-i-1], s[i]
print("".join(s))

# 5
ans = ""
s3 = list(s3)
while s3:
    ans += s3.pop(-1)
print(ans)

# 6
for i in range(len(s2)):
    print(s2[-i-1], end="")
print()
# 7
s2 = list(s2)
while s2:
    print(s2.pop(), end="")
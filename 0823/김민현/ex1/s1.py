a = '2+3*4/5'
ans = ''
stack = []
for i in a:
    try:
        ans += str(int(i))
    except:
        stack.append(i)

for j in range(len(stack)):
    ans += stack.pop(-1)
print(ans)

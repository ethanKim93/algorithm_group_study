a = "2+3*4/5"
stack = []
tmp = ''
pr = ['/','*']
for i in a:
    if i.isdecimal():
        tmp+= i
    elif i not in pr:
        while stack and stack[-1] in pr:
            tmp += stack.pop()
        stack.append(i)
    else:
        stack.append(i)

while stack:
    tmp += stack.pop()

# 계산식
stack2 = []
for j in tmp:
    oper = ''
    if j.isdecimal():
        stack2.append(j)
    else:
        b = stack2.pop()
        a = stack2.pop()
        result = eval('{}{}{}'.format(a, j, b))
        stack2.append(result)

print(stack2)


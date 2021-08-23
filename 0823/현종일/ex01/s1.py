a = "2+3*4/5"
stack = []
tmp = []
pr = ['/','*']
for i in a:
    if i.isdecimal():
        tmp.append(i)
    elif i not in pr:
        while stack and stack[-1] in pr:
            tmp.append(stack.pop())
        stack.append(i)
    else:
        stack.append(i)

while stack:
    tmp.append(stack.pop())


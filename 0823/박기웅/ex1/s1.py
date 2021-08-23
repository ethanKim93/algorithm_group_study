formula = '2+3*4/5'
stack = []
for i in formula:
    if i == '+':
        stack.append(i)
    elif i == '-':
        stack.append(i)
    elif i == '*':
        stack.append(i)
    elif i == '/':
        stack.append(i)
    else:
        print(i,end='')

while(stack):
    print(stack.pop(), end='')
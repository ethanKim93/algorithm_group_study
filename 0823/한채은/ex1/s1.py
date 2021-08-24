
S = input()
stack = []
for i in S:
    if i == '+':
        stack.append(i)
    elif i == '-':
        stack.append(i)
    elif i == '*':
        stack.append(i)
    elif i == '/':
        stack.append(i)
    else:
        print(i, end='')

while stack:
    print(stack.pop(), end='')
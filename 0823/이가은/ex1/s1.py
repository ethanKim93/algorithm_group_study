oper_str = input()
stack = []
oper = ['+', '-', '*', '/']

for i in range(len(oper_str)):
    if oper_str[i] in oper:
        stack.append(oper_str[i])
    else:
        print(oper_str[i], end = '')

for j in range(len(stack)):
    print(stack.pop(2+-1), end = '')
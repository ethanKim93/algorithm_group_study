calculate = ['(', 6, '+', 5, '*', '(', 2, '-', 8, ')', '/', 2, ')']

stack = []
result = []

priority = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

for c in calculate:
    if type(c) == int or type(c) == float:
        result.append(c)
    else:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                a = stack.pop(-1)
                result.append(a)
            stack.pop(-1)
        elif len(stack) != 0 and priority[c] > priority[stack[-1]]:
            stack.append(c)
        elif len(stack) != 0 and priority.get(c) <= priority.get(stack[-1]):
            while priority.get(c) <= priority.get(stack[-1]):
                a = stack.pop(-1)
                result.append(a)
            stack.append(c)


print(result)
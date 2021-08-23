def push(item):
    stack.append(item)

def pop():
    return stack.pop()

formula = '2 + 3 * 4 / 5'
formula = list(formula.split())
# print(formula)
stack = []

for a in formula:
    if a == '+' or a == '*' or a == '/':
        push(a)
    else:
        print(a, end='')
else:
    while len(stack):
        result = pop()
        print(result, end='')
# print(stack)
# print(result)
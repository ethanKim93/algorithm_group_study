expression = input().split(' ')
stack = []
answer = []
for oper in expression:
    if oper == '+' or oper == '-' or oper == '*' or oper == '/':
        stack.append(oper)
    else:
        answer.append(oper)
while stack:
    answer.append(stack.pop())

print(*answer)

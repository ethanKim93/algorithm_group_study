expression = input()  # 2+3*4/5
operation_list = ['+', '-', '*', '/']
stack = []

for i in expression:
    if i not in operation_list:
        print(i, end='')
    else:
        stack.append(i)

for i in range(len(stack)):
    print(stack.pop(), end='')



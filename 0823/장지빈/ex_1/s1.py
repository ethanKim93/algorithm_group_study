mod = ['2', '+', '3', '*', '4', '/', '5']
cal = ['*', '-', '/', '+']
stack = []
i = 0
for i in mod:
    if i in cal:
        stack.append(i)
    else:
        print(i, end = ' ')
for j in range(len(stack)):
    print(stack.pop(), end = ' ')
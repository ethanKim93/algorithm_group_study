string = '2+3*4/5'
stack = []
for i in range(len(string)):
    if string[i] not in '/*-+':
        print(string[i], end=" ")
    else:
        stack.append(string[i])

for i in range(len(stack)):
    print(stack.pop(), end=" ")
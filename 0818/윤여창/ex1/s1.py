a = [1,2,3]
stack = [0]*3
top = 0
for i in a:
    stack[top] = i
    top += 1

for i in range(3):
    top -= 1
    print(stack.pop(top))
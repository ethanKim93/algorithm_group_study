# 1
stack = []
data = [1, 2, 3]
for i in data:
    stack.append(i)

for _ in range(3):
    print(stack.pop())

# 2

top = 0
stack = [0] * 4
for i in data:
    stack[top] = i
    top += 1

# stack = [1, 2, 3, 0]

for i in range(3):
    top -= 1
    print(stack.pop(top))

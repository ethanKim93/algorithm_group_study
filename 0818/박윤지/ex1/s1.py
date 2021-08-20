def push(item):
    stack.append(item)


def pop():
    if len(stack) == 0:
        # underflow
        return
    else:
        return stack.pop(-1)


stack = []

push(1)
push('d')
push(88)
print(stack)

pop()
pop()
pop()
print(stack)

def push(item):
    global stack
    stack += [item]
    return None
def pop():
    global stack
    if len(stack) != 0:
        item = stack[-1]
        stack = stack[:-1]
        return item
    else:
        return -1

stack = []
push(1)
push(2)
push(3)
print(stack)

print(pop())
print(pop())
print(pop())
stack = [0] * 10
top = -1


def push(n):
    global top
    top += 1
    stack[top] = n


def pop():
    global top
    top -= 1
    return stack[top+1]


push(1)
push(2)
push(3)
a = pop()
b = pop()
c = pop()
print(a, b, c)
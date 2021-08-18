top = -1
s = [0] * 10

def push(item):
    global top
    top += 1
    s[top] = item

def pop():
    global top
    if top > -1:
        top -= 1
        s[top + 1] = 0
        return s[top + 1]
    else:
        return

print(s)
push(2)
print(s)
push(5)
print(s)
print(pop())
print(s)
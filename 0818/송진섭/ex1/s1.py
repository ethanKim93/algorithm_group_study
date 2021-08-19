def push(item):
    global s
    global top

    top += 1
    s[top] = item


def pop():
    global s

    if s[0] == 0:
        return
    else:
        return s.pop(-1)


top = -1
s = [0] * 3
push(1)
push(2)
push(3)
pop()
print(s)
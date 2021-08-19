s = []

def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        return
    else:
        return s.pop(-1)

push(1)
push(2)
push(3)
print(s)
pop()
pop()
pop()
print(s)
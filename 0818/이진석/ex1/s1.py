s = []
def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        return
    else:
        return s.pop(-1)

push(5)
print(s)
pop()
print(s)
push(5)
print(s)
pop()
print(s)
push(5)
print(s)
push(5)
print(s)

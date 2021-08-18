def push(item):
    s.append(item)


def pop(s):
    if len(s) == 0:
        return 'EMPTY'
    else:
        return s.pop(-1)


s = []
push(3)
push(2)
push(1)
print(s.pop(-1))
print(s.pop(1))
print(s.pop(0))

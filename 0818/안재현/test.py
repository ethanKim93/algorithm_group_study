def push(item):
    s.append(item)


def pop(s):
    if len(s) == 0:
        return 'EMPTY'
    else:
        return s.pop(-1)


s = []
s.append(1)
s.append(2)
s.append(3)
print(s.pop(1))

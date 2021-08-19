def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        return print('stack이 비었습니다')

    else:
        return s.pop(-1)

s = []
push('A')
push('B')
push('C')
pop()
pop()
pop()
pop()
print(s)
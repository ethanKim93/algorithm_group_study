lst = []

def push(item):
    lst.append(item)

def pop():
    if len(lst) == 0:
        return
    else:
        return lst.pop(-1)


push(3)
push(4)
push(5)
print(lst)
pop()
pop()
pop()
print(lst)

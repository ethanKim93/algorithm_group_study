# ex1 - 스택 구현
s = []


def push(item):
    s.append(item)


def my_pop():
    if not len(s):
        # underflow
        return
    else:
        return s.pop()


for i in range(3):
    push(i)

for _ in range(3):
    print(my_pop())
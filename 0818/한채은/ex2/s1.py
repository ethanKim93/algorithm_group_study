import sys
sys.stdin = open("input.txt")


def push(item):
    llist.append(item)


def pop():
    if llist == 0:
        return
    else:
        return llist.pop()


def is_empty(llist):
    if not llist:
        return True
    return False


for i in range(2):
    tc = input()
    llist = []
    for j in tc:
        if j == '(':
            push(j)
        if j == ')':
            pop()

    print(is_empty(llist))
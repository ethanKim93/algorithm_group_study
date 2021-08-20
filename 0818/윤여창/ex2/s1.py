import sys
sys.stdin = open("input.txt")

def pop():
    if len(a) == 0:
        return
    else:
        return a.pop()

def push(x):
    a.append(x)


def find(arr):
    if len(a) != 0 :
        return True
    else:
        return False

for i in range(2):
    sttr = input()
    a = []
    for b in sttr:
        if b == '(':
            push(b)
        if b == ')':
            pop()

    print(find(a))
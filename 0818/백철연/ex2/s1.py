

def f(b):
    arr = []
    for s in b:
        if s == '(':
            arr.append(s)
        elif s == ')':
            if len(arr) == 0:
                return 0
            arr.pop()
    if len(arr) != 0:
        return 0

    return 1


import sys
sys.stdin = open('input.txt')

n1 = input()
n2 = input()

print(f(n2))

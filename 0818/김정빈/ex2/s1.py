import sys
sys.stdin = open("input.txt")

def push(i):
    B.append(i)

def pop():
    if len(B) == 0:
        return
    else:
        return B.pop(-1)
def isempty(arr):
    if not len(B):
        return True
    return False

for _ in range(2):
    brackets = input()
    B = []
    for b in brackets:
        if b == '(':
            push(b)
        if b == ')':
            pop()

    print(isempty(B))
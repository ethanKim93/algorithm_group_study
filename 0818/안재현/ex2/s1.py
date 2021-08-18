import sys

sys.stdin = open('input.txt')

for a in range(2):
    N = input()
    empty = []
    result = True
    for i in range(len(N)):
        if len(empty) == 0:
            if N[i] == '(':
                empty.append(N[i])
            elif N[i] == ')':
                result = False
        elif N[i] == '(':
            empty.append(N[i])
        elif N[i] == ')':
            if empty[-1] == '(':
                empty.pop(-1)
            elif N[i] == ')':
                result = False
    if len(empty) != 0:
        result = False
    print(result)

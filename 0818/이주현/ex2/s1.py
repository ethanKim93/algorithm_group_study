import sys
sys.stdin = open("input.txt")

for i in range(2):
    N = input()

    stack = []
    count = 0
    for i in range(len(N)):
        if N[i] == '(':
            stack += [N[i]]
        else:
            stack = stack[:-1]
            count +=1

    print(count)
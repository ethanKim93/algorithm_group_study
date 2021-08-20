import sys

sys.stdin = open("sample_input.txt")

result = 0


def popping(empty):
    global result
    if len(empty) == 0:
        return 1
    elif len(empty) != 0:
        for j in range(len(empty) - 1):
            if empty[j] == '(' and empty[j + 1] == ')':
                empty.pop(j)
                empty.pop(j)
                return popping(empty)
            elif empty[j] == '{' and empty[j + 1] == '}':
                empty.pop(j)
                empty.pop(j)
                return popping(empty)
            else:
                result = 1
    if result == 1:
        return 0


T = int(input())
for tc in range(0, T):
    N = input()
    # print(N)
    empty = []
    switch = 0
    for i in range(len(N)):
        # print(i)
        if N[i] == "'":
            switch += 1
        elif switch % 2 == 0:
            if N[i] == '(' or N[i] == '{':
                empty.append(N[i])
            elif N[i] == ')' or N[i] == '}':
                empty.append(N[i])

    print('#{} {}'.format(tc + 1, popping(empty)))

import sys
sys.stdin = open('input.txt')


def push(item):
    stack.append(item)


def pop():
    if len(stack) == 0:
        # underflow
        return
    else:
        return stack.pop(-1)


def match(test):
    for t in test:
        if t in ['(', '[', '{']:
            push(t)
        elif t in [')', ']', '}']:
            try:
                former = pop()
                if (former == '(' and t == ')') or (former == '[' and t == ']') or (former == '{' and t == '}'):
                    pass
                else:
                    return False
            except:
                return False
    if len(stack) != 0:
        return False
    return True


stack = []

for tc in range(2):
    test = input()
    print(match(test))

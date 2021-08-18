# ex2 - 괄호 검사
import sys
sys.stdin = open('input.txt')


def push(item):
    s.append(item)


def pop():
    if not len(s):
        # underflow
        return
    else:
        return s.pop()


def check(p):
    for char in p:
        if char == '(':
            push('(')
        elif char == ')':
            if not pop():
                return False
    if len(s):
        return False
    else:
        return True


for _ in range(2):
    p = input()
    s = []
    print(check(p))


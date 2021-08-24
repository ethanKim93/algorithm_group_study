import sys
sys.stdin = open('input.txt')

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

for tc in range(1,11):
    N = int(input())
    cal = input()
    stack = []
    num = ''

    for idx,ch in enumerate(cal):
        if ch not in prec.keys():
            num += ch
        if ch == '*':
            stack.append(ch)
        else:
            while stack:
                num += stack.pop(-1)
            stack.append(ch)
    for i in stack:
        num += i

    stack2 = []
    result = 0
    for k in num:

        if k not in prec.keys():
            stack2.append(int(k))
        else:
            if k == '+':
                a = stack2.pop()
                b = stack2.pop()
                c = a+b
                stack2.append(c)
            elif k == '*':
                a = stack2.pop()
                b = stack2.pop()
                c = a*b
                stack2.append(c)
            p = stack2
            q = k
            w =1
    result = stack2.pop()
    print(result)
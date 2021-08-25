import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    string = input()

    postfix = []
    cal = []

    for i in range(len(string)):
        if string[i] == '(':
            cal.append(string[i])
        elif string[i] in '0123456789':
            postfix.append(string[i])
        elif string[i] in '/*-+':
            if cal:
                if string[i] in '/*':
                    while cal[-1] not in '+-(':
                        postfix.append(cal.pop())
                        if not cal:
                            break
                    cal.append(string[i])
                else:
                    while cal[-1] != '(':
                        postfix.append(cal.pop())
                        if not cal:
                            break
                    cal.append(string[i])
            else:
                cal.append(string[i])
        else:
            if cal:
                while cal[-1] != '(':
                    postfix.append(cal.pop())
                    if not cal:
                        break
                cal.pop()

    for i in range(len(postfix)):
        if postfix[i] == '+':
            b = int(cal.pop())
            a = int(cal.pop())
            cal.append(a + b)
        elif postfix[i] == '-':
            b = int(cal.pop())
            a = int(cal.pop())
            cal.append(a - b)
        elif postfix[i] == '*':
            b = int(cal.pop())
            a = int(cal.pop())
            cal.append(a * b)
        elif postfix[i] == '/':
            b = int(cal.pop())
            a = int(cal.pop())
            cal.append(a / b)
        else:
            cal.append(postfix[i])

    print("#{} {}".format(tc, cal[0]))
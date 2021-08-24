import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    opt_str = input()

    stk1 = []
    calc = []

    for idx in range(len(opt_str)):
        if opt_str[idx] == '*':
            while True:
                if not stk1 or stk1[-1] == '+':
                    stk1.append(opt_str[idx])
                    break
                else:
                    calc.append(stk1.pop())

        elif opt_str[idx] == '+':
            while True:
                if not stk1:
                    stk1.append(opt_str[idx])
                    break
                else:
                    calc.append(stk1.pop())
        else:
            calc.append(opt_str[idx])
    while stk1:
        calc.append(stk1.pop())

    stk2 = []

    for c in range(len(calc)):
        if calc[c] == '+':
            a = stk2.pop()
            b = stk2.pop()
            res = b + a
            stk2.append(res)

        elif calc[c] == '*':
            a = stk2.pop()
            b = stk2.pop()
            res = b * a
            stk2.append(res)

        else:
            stk2.append(int(calc[c]))
    print('#{} {}'.format(tc, stk2.pop()))

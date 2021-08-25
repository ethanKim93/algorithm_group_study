import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = list(input())
    # print(arr)

    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    stack = []
    operand = []
    for a in arr:
        if a == '(':
            operand.append(a)
        elif a == ')':
            tmp = operand.pop()
            while tmp != '(':
                stack.append(tmp)
                tmp = operand.pop()
        elif a in '+-/*^':
            while operand and (prec[operand[-1]] >= prec[a]):
                stack.append(operand.pop())
            operand.append(a)

        else:
            stack.append(a)

    while operand:
        stack.append(operand.pop())

    for st in stack:
        if st.isdecimal():
            operand.append(int(st))
        else:
            if st == '+':
                num1 = operand.pop()
                if not operand:
                    operand.clear()
                    break
                num2 = operand.pop()
                operand.append(num2 + num1)
            elif st == '*':
                num1 = operand.pop()
                if not operand:
                    operand.clear()
                    break
                num2 = operand.pop()
                operand.append(num2 * num1)
            elif st == '-':
                num1 = operand.pop()
                if not operand:
                    operand.clear()
                    break
                num2 = operand.pop()
                operand.append(num2 - num1)
            elif st == '/':
                num1 = operand.pop()
                if not operand:
                    operand.clear()
                    break
                num2 = operand.pop()
                operand.append(num2 // num1)

    result= ''.join(map(str,operand))
    print('#{} {}' .format(tc,result))
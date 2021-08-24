import sys
sys.stdin = open('input.txt')

for tc in range(10):
    oper_len = int(input())
    oper_inp = input()

    # 후위연산자 구현하기
    oper_str = ''
    oper_stack = []
    i = 0

    while i < oper_len:
        if oper_inp[i] == '+':
            while oper_stack:
                oper_str += oper_stack.pop(-1)
            oper_stack.append(oper_inp[i])
        elif '0' <= oper_inp[i] <= '9':
            oper_str += oper_inp[i]
        else:
            oper_stack.append(oper_inp[i])
        i += 1
    while oper_stack:
        oper_str += oper_stack.pop(-1)

    num_li = []
    i = 0
    while i < len(oper_str):
        if oper_str[i] == '*':
            n1 = num_li.pop()
            n2 = num_li.pop()
            num_li.append(n1*n2)
        elif oper_str[i] == '+':
            n1 = num_li.pop()
            n2 = num_li.pop()
            num_li.append(n1+n2)
        else:
            num_li.append(int(oper_str[i]))
        i += 1

    print('#{} {}'.format(tc+1, *num_li))
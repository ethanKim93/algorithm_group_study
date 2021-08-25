import sys
sys.stdin = open('input.txt')

def postfix(oper_str):
    df_result = ''
    df_stack = []
    for i in range(len(oper_str)):
        if '0' <= oper_str[i] <= '9':
            df_result += oper_str[i]
        elif oper_str == '+':
            while df_stack:
                oper_str += df_stack.pop()
            df_stack.append('+')
        elif oper_str == '*':
            df_stack.append('*')
    while df_stack:
        df_result += df_stack.pop()
    return df_result


for tc in range(10):
    N = int(input())
    operation = input()

    while ')' not in operation:
        for i in range(len(operation)):
            if operation[i] == ')':
                for j in range(i,-1,-1):
                    if operation[j] == '(':
                        a = j
                        break
                break
        new = postfix(operation[i-a+1:a-1])
        operation = ''.join((operation[:i-a],new,operation[a:]))
    print(operation)


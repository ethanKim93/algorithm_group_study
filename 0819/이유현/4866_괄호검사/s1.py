import sys
sys.stdin = open('sample_input.txt')


def check_p(p_list):
    stk = []
    for p in p_list:
        if p == '(' or p == '{':
            stk.append(p)
        else:
            if p == ')' or p == '}':
                if not stk:
                    return 0
                elif (p == ')' and stk[-1] != '(') or (p == '}' and stk[-1] != '{'):
                    return 0
                else:
                    stk.pop()
    if not stk:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    cmd = input()
    p_list = []
    for c in cmd:
        if c == '(' or c == ')' or c == '{' or c == '}':
            p_list.append(c)
    print('#{} {}'.format(tc, check_p(p_list)))


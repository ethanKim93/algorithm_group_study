import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    top = -1
    pars = input()
    pars_list = []
    result = 1
    for par in pars:
        if par == '(' or par =='{':
            pars_list.append(par)
            top += 1
        if par == ')' or par == '}':
            if len(pars_list) > 0:
                if pars_list[top] == '(' if par == ')' else '{':
                    pars_list.pop()
                    top -= 1
                else:
                    result = 0
                    break
            else:
                result = 0
                break

    if len(pars_list) > 0:
        result = 0

    print('#{} {}'.format(tc, result))



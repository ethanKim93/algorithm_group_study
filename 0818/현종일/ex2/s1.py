import sys
sys.stdin = open('input.txt')

for _ in range(2):
    pars = input()
    pars_list = []
    for par in pars:
        if par == '(':
            pars_list.append(par)
        elif par == ')':
            pars_list.pop()

    print(True if len(pars_list) == 0 else False)
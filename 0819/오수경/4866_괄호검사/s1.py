import sys
sys.stdin = open('sample_input.txt', 'rt', encoding='UTF8')

T = int(input())
for tc in range(1, T+1):
    fix_str = input()
    s = []

    for item in fix_str:
        if item == '(' or item == '{':
            s.append(item)

        elif item == ')':
            if len(s) == 0 or s[-1] != '(':
                s.append('0')
                break
            elif s[-1] == '(':
                s.pop(-1)


        elif item == '}':
            if len(s) == 0 or s[-1] != '{':
                s.append('0')
                break

            elif s[-1] == '{':
                s.pop(-1)


    if s:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, 1))
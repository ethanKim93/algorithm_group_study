import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    V, E = list(input().split())
    c_list = ''

    for i in E:
        if c_list and c_list[-1] != i:
            c_list += i
        elif c_list:
            c_list = c_list[:-1]
        else:
            c_list += i

    print('#{} {}'.format(tc, c_list))
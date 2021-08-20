import sys
sys.stdin = open('input.txt')


def dup(w_list):
    i = 0
    while i < len(w_list) - 1:
        if w_list[i] == w_list[i+1]:
            w_list.pop(i)
            w_list.pop(i)
            dup(w_list)
        else:
            i += 1
    return w_list


for tc in range(1, 11):
    N, pwd = input().split()
    pwd = list(pwd)

    print('#{}'.format(tc), end=' ')
    for p in dup(pwd):
        print(p, end='')
    print()
import sys
sys.stdin = open('sample_input.txt')

def dup(w_list):
    i = 0
    while i < len(w_list) - 1:
        if w_list[i] == w_list[i+1]:
            w_list.pop(i)
            w_list.pop(i)
            dup(w_list)
        else:
            i += 1
    return len(w_list)


T = int(input())
for tc in range(1, T+1):
    str_list = list(input())
    print('#{} {}'.format(tc, dup(str_list)))
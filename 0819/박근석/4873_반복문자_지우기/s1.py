import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    K = input()
    c_list = []

    for i in K:
        if len(c_list) != 0 and c_list[-1] != i:
            c_list.append(i)
        elif len(c_list) != 0:
            c_list.pop()
        else:
            c_list.append(i)

    print('#{} {}'.format(tc, len(c_list)))




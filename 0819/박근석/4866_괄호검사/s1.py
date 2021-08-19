import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def check(s_list):
    c_list = []

    for i in range(len(s_list)):
        if s_list[i] == '(' or s_list[i] == '{':
            c_list.append(s_list[i])
        elif len(c_list) != 0 and c_list[-1] == '(' and s_list[i] == ')':
            c_list.pop()
        elif len(c_list) != 0 and c_list[-1] == '{' and s_list[i] == '}':
            c_list.pop()
        elif len(c_list) == 0 and (s_list[i] == ')' or s_list[i] == '}'):
            return 0

    return 0 if c_list else 1

for tc in range(1, T+1):
    K = list(input())
    print('#{} {}'.format(tc, check(K)))
import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t + 1):
    s = input()
    bin_list = []
    for i in s:
        if i == '(' or i == '{':
            bin_list.append(i)

        elif i == ')':
            if len(bin_list) == 0 or bin_list[-1] != '(':
                bin_list.append('end')
                break
            elif bin_list[-1] == '(':
                bin_list.pop()

        elif i == '}':
            if len(bin_list) == 0 or bin_list[-1] != '{':
                bin_list.append('end')
                break
            elif bin_list[-1] == '{':
                bin_list.pop()

    if len(bin_list) > 0 :
        print("#{} {}".format(tc, 0))
    else:
        print("#{} {}".format(tc, 1))
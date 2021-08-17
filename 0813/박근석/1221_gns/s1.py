import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(input().split())
    list_a = list(input().split())

    list_b = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    num_list = [0]*10
    for i in list_a:
        # print(i)
        if i == list_b[0]:
            num_list[0] += 1
        elif i == list_b[1]:
            num_list[1] += 1
        elif i == list_b[2]:
            num_list[2] += 1
        elif i == list_b[3]:
            num_list[3] += 1
        elif i == list_b[4]:
            num_list[4] += 1
        elif i == list_b[5]:
            num_list[5] += 1
        elif i == list_b[6]:
            num_list[6] += 1
        elif i == list_b[7]:
            num_list[7] += 1
        elif i == list_b[8]:
            num_list[8] += 1
        else:
            num_list[9] += 1

    result_string = ''
    for i in range(10):
        result_string += (list_b[i] + ' ')*num_list[i]

    print('#{} {}'.format(tc, result_string[:-1]))

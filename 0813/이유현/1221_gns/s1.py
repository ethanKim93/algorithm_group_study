import sys
sys.stdin = open('GNS_test_input.txt', encoding='UTF-8')

T = int(input())
for i in range(1, T+1):
    tn, tlen = input().split()
    # tc = input().split()

    ex = input()
    numstr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    cnt = 0
    num_list = []
    for i in range(10):
        cnt = ex.count(numstr[i])
        num_list += [numstr[i]] * cnt
    print(tn)
    print(*num_list)
import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for _ in range(T):
    tc, l = map(str,input().split(' '))
    li = list(map(str, input().split()))
    result = []
    p = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN','EGT','NIN']
    for i in range(len(p)):
        for j in range(len(li)):
            if p[i] == li[j] :
                result.append(li[j])
    li_sort = ' '.join(map(str, result))
    print('{} {}'.format(tc,li_sort))

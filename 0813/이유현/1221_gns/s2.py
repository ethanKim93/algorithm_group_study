import sys
sys.stdin = open('GNS_test_input2.txt', encoding='UTF-8')

tn, tlen = input().split()
ex = input()
numstr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
cnt = 0
num_list = []
for i in range(10):
    cnt = ex.count(numstr[i])
    num_list += [numstr[i]] * cnt
print(tn)
print(*num_list)



# tc = input().split()
# ex = list(input().split())
# numstr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
#
# n = 0
# num_list = []
#
# for word in ex:
#     for idx in range(10):
#         wton = word.replace(numstr[idx], str(idx))
#         num_list.append(wton)
# print(num_list)

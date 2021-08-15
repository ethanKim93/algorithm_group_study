import sys
sys.stdin = open("GNS_test_input.txt")

test_case = int(input())
for _ in range(test_case):
    test_num, test_len = input().split()

    # test_len의 개수만큼 test_words에 단어들을 list 형태로 저장
    test_words = list(map(str, input().split()))

    # 그 후...노가다... :)

    result_list= []
    for z in test_words:
        if z == 'ZRO':
            result_list.append('ZRO')

    for o in test_words:
        if o == 'ONE':
            result_list.append('ONE')

    for t in test_words:
        if t == 'TWO':
            result_list.append('TWO')

    for th in test_words:
        if th == 'THR':
            result_list.append('THR')

    for f in test_words:
        if f == 'FOR':
            result_list.append('FOR')

    for fi in test_words:
        if fi == 'FIV':
            result_list.append('FIV')

    for s in test_words:
        if s == 'SIX':
            result_list.append('SIX')

    for sv in test_words:
        if sv == 'SVN':
            result_list.append('SVN')

    for e in test_words:
        if e == 'EGT':
            result_list.append('EGT')

    for n in test_words:
        if n == 'NIN':
            result_list.append('NIN')

    result_str = ' '.join(result_list)
    print('{}\n{}'.format(test_num, result_str))



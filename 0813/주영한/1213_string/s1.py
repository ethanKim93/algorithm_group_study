import sys
sys.stdin = open("test_input.txt", encoding='UTF8')

"""
**************Brute Force****************
"""


def bruteforce(main_str, cmp_str):
    cnt = 0
    LM = len(main_str)
    LC = len(cmp_str)
    for i in range(LM - LC + 1):
        for j in range(LC):
            if main_str[i + j] != cmp_str[j]:
                break
            if j == LC - 1:
                cnt += 1
    return cnt


for tc in range(1, 11):
    dummy = input()
    cmp_str = input()
    main_str = input()
    print("#{} {}".format(tc, bruteforce(main_str, cmp_str)))

import sys
sys.stdin = open("test_input.txt", encoding='UTF8')


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

def generatenext(cmp_str):
    LC = len(cmp_str)
    cmp_next = [-1] * LC
    main_idx = 1
    sub_idx = 0
    while main_idx < LC:
        if cmp_str[main_idx] == cmp_str[sub_idx]:
            sub_idx += 1
            cmp_next[main_idx] = sub_idx
            main_idx += 1
        else:
            if sub_idx != 0:
                sub_idx = cmp_next[sub_idx - 1]
            else:
                cmp_next[main_idx] = 0
                main_idx += 1
    return cmp_next

# def kmp(main_str, cmp_str):
#     cnt = 0
#     LM = len(main_str)
#     LC = len(cmp_str)
#     cmp_next = generatenext(cmp_str)
#     idx = 0
#     while idx < LM:
#         for i in range(LC):
#             if main_str[idx + i] != cmp_str[idx]:
#                 idx =
#                 break
#             if i == LC - 1:
#                 cnt += 1
#



for tc in range(1, 11):
    dummy = input()
    cmp_str = input()
    main_str = input()
    print("#{} {}".format(tc, bruteforce(main_str, cmp_str)))



#
#

#
# def boyermoore(main_str, cmp_str):
#     pass

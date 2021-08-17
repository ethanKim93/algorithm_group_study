import sys
sys.stdin = open("test_input.txt", encoding='UTF8')

"""
**************KMP****************
"""


# nextM을 생성하는 코드이다.
def generatenext(cmp_str):
    LC = len(cmp_str)
    cmp_next = [-1] * LC

    # main_idx = 0일 경우, cmp_str간의 비교가 의미가 없다.
    # 1(2345) 와 (12345)를 비교하기 위해서이다.
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


def kmp(main_str, cmp_str):
    cnt = 0
    LM = len(main_str)
    LC = len(cmp_str)
    cmp_next = generatenext(cmp_str)
    idx = 0

    while idx < LM - LC + 1:
        for i in range(LC):
            if main_str[idx + i] != cmp_str[i]:
                idx += i - cmp_next[i]
                break
            if i == LC - 1:
                cnt += 1
                idx += LC
    return cnt


for tc in range(1, 11):
    dummy = input()
    cmp_str = input()
    main_str = input()
    print("#{} {}".format(tc, kmp(main_str, cmp_str)))

import sys
sys.stdin = open("test_input.txt", encoding='UTF8')

"""
**************Boyer-Moore****************
"""


def find_element(text, cmp_str):
    # 문자열의 비교 글자를 인자 text로 받고, cmp_str와 같은 글자가 있는지 찾는다.
    # 범위의 경우, range(len(cmp_str) - 1)이고, cmp_str의 마지막 글자의 경우 빼준다. (만약 넣어줄 경우 계속 반복된다)
    for sub_idx in range(len(cmp_str) - 1):

        # 만약 문자열의 비교 글자와 같은 글자가 cmp_str에 있을 경우,
        # 해당 글자 위치를 문자열의 비교 글자와 동일선 상에 맞추기 위해 이동 거리를 반환해준다.
        if text == cmp_str[sub_idx]:
            return len(cmp_str) - sub_idx - 1

    # 문자열의 비교 글자와 같은 글자가 cmp_str에 없을 경우,
    # cmp_str의 길이만큼 이동시켜준다.
    return len(cmp_str)


def boyermoore(main_str, cmp_str):
    cnt = 0
    LM = len(main_str)
    LC = len(cmp_str)
    idx = LC - 1
    while idx < LM:
        # 문자열과 비교 문자열의 마지막와 같지 않을 경우,
        if main_str[idx] != cmp_str[LC - 1]:
            # 비교 문자열 중에 해당 문자와 같은 문자가 있는지 찾고, 같은 인덱스로 이동시킨다.
            idx += find_element(main_str[idx], cmp_str)
            continue

        # 문자열과 비교 문자열의 마지막와 같은 경우,
        else:
            # 해당 비교 문자열을 마지막으로 하고 길이가 cmp_str 만큼의 비교 문자열과 cmp_str를 비교한다.
            for sub_idx in range(LC):
                # 만약 다를 경우, cmp_str 내에 다른 비교 문자열의 글자가 있는지 확인한다.
                if main_str[idx - LC + 1 + sub_idx] != cmp_str[sub_idx]:
                    idx += find_element(main_str[LC - idx + sub_idx], cmp_str)
                    break

                # 다 같을 경우, cnt를 하나 증가시켜주고, cmp_str의 길이만큼 이동시킨다.
                if sub_idx == LC - 1:
                    cnt += 1
                    idx += LC
    return cnt


for tc in range(1, 11):
    dummy = input()
    cmp_str = input()
    main_str = input()
    print("#{} {}".format(tc, boyermoore(main_str, cmp_str)))

import sys
sys.stdin = open('test_input.txt', 'rt', encoding='UTF8')


# 고지식한 패턴
def find_str (find, str_eng):
    s = 0
    f = 0
    while f < len(find) and s < len(str_eng):
        if str_eng[s] != find[f]:
            s = s - f
            f = -1
        s = s + 1
        f = f + 1
    if f == len(find):
        return 1 + find_str(find, str_eng[s-len(find)+1:])
    else:
        return 0

for tc in range(1, 11):
    test_num = input()
    find = input()
    str_eng = input()
    print('#{} {}'.format(tc, find_str(find, str_eng)))






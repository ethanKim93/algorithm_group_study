import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    cnt = 0
    cnt_table = dict()
    cmp_str = input()
    main_str = input()
    for text in main_str:
        if cnt_table.get(text):
            cnt_table[text] += 1
        else:
            cnt_table[text] = 1

    for text in cmp_str:
        if cnt_table.get(text):
            temp_cnt = cnt_table[text]
            if cnt < temp_cnt:
                cnt = temp_cnt
    print("#{} {}".format(tc, cnt))
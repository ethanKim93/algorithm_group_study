import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str1_dic = {}
    str2_dic = {}

    for i in str1:
        str1_dic[i] = True

    for j in str1_dic:
        for k in str2:
            if j == k:
                if str2_dic.get(j):
                    str2_dic[j] += 1
                else:
                    str2_dic[j] = 1
    cnt_max = 0
    for val in str2_dic.values():
       if val > cnt_max:
           cnt_max = val

    print('#{} {}'.format(tc, cnt_max))
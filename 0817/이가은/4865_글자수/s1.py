import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for test in range(T):

    str1 = str(input())
    str2 = str(input())

    N = len(str1)
    M = len(str2)
    result_dic = {}

    for spell in str1: # key에 해당하는 값 생성
        if spell not in result_dic:
            result_dic[spell] = 0

    for spell in str2: #key가 str2에 있으면 +1 증가
        if spell in result_dic:
            result_dic[spell] += 1

    print('#{} {}'.format(test+1, max(result_dic.values())))
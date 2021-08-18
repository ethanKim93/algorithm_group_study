import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    str1 = str(input())
    str2 = str(input())

    dic_str1 ={}
    for i in str1:
        dic_str1[i] = 0

    for i in range(len(str2)):
        for j in range(len(str1)):
            if str2[i] == str1[j]:
                dic_str1[str1[j]] += 1
                break
    max_num = 0
    for value in dic_str1.values():
        if max_num < value:
            max_num = value
    print('#{} {}'.format(tc,max_num))

import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    str1 = str(input())
    str2 = str(input())
    result = 0
    cnt = 0
    pass_num  = 0
    for i in range(0,len(str2)):
        if pass_num > 0:
            pass_num -= 1
            continue
        if str2[i] == str1[cnt]:
                cnt += 1
        else:
            pass_num = cnt
            cnt = 0
        if cnt == len(str1):
            result = 1
            break

    print('#{} {}'.format(tc,result))
import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    str1 = str(input())
    str2 = str(input())
    result = 0
    cnt = 0
    i = 0
    while i < len(str2):
        if str2[i] == str1[cnt]:
                cnt += 1
        else:
            i += cnt
            cnt = 0
        #동일한 문자열을 찾았다면.
        if cnt == len(str1):
            result = 1
            break
        i += 1

    print('#{} {}'.format(tc,result))
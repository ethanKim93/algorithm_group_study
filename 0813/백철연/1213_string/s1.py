import sys
sys.stdin = open('test_input.txt','r',encoding='utf-8' )


for tc in range(1,11):
    n = int(input())
    k = input()       #비교할 문자
    find = input()    #문자열
    result = 0

    for i in range(len(find)):
        if find[i] == k[0]:
            if find[i:i+len(k)] == k:
                result += 1
    print('#{} {}'.format(tc,result))

import sys
sys.stdin = open('test_input.txt',encoding='UTF8')

for i in range(1,11):
    tc = int(input())
    f_str = str(input())
    base_str = str(input())

    result = 0
    for i in range(len(base_str)-len(f_str)+1):
        cnt = 0
        for j in range(len(f_str)):
            if base_str[i+j] == f_str[j]:
                cnt += 1
        if cnt == len(f_str):
            result += 1
    print('#{} {}'.format(tc,result))
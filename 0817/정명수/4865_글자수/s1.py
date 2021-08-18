import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    str1 = input()
    str2 = input()
    str1 = set(str1)
    counter={}
    for i in str2:
        if i in str1:
            try:
                counter[i] += 1
            except:
                counter[i] = 1
    max_value = 0
    for key,value in counter.items():
        if value>max_value:
            max_value = value
    print('#{} {}'.format(test_case,max_value))

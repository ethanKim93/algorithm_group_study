# int(숫자, 2) 사용

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n2 = input()
    n3 = input()
    # 2진수
    len2 = len(n2)
    n210 = int(n2, 2)
    set2 = set()
    for i in range(len2):
        set2.add(n210 ^ (1 << i))
    # 3진수
    len3 = len(n3)
    n310 = int(n3, 3)
    set3 = set()
    for j in range(len3):
        temp = n310 - (3**j * int(n3[len3-j-1]))
        if n3[len3-j-1] == '0':
            temp1 = temp + (3**j * 2)
            temp2 = temp + (3**j * 1)
            set3.add(temp1)
            set3.add(temp2)
        if n3[len3-j-1] == '1':
            temp1 = temp + (3**j * 0)
            temp2 = temp + (3**j * 2)
            set3.add(temp1)
            set3.add(temp2)
        if n3[len3-j-1] == '2':
            temp1 = temp + (3**j * 1)
            temp2 = temp + (3**j * 0)
            set3.add(temp1)
            set3.add(temp2)
    # print(set3)
    # print(set2)
    # print(set2 & set3)

    for k in set3:
        if k in set2:
            ans = k

    print('#{} {}'.format(tc, ans))

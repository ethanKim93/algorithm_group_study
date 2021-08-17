#실행 시간 : 0.28700s  0.30619s

import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for i in range(1,T+1):
    tc= list(input().split())
    in_str = list(map(str,input().split()))
    str_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_count = [0]*10

    for i in in_str:
        for j in range(len(str_list)):
            if i == str_list[j]:
                 num_count[j] += 1
    
    print(tc[0])
    for i in range(len(str_list)):
        for j in range(num_count[i]):
            print(str_list[i],end=' ')

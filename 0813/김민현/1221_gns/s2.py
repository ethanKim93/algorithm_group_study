#실행 시간 : 0.36793s  0.36668s
import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for i in range(1,T+1):
    tc= list(input().split())
    in_str = str(input())
    str_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_count = [0]*10
    for i in range(len(in_str)-2):
        for k in range(len(str_list)):
            cnt = 0
            for j in range(len(str_list[k])):
                if in_str[i+j] == str_list[k][j]:
                    cnt += 1
                else:
                    break
            if cnt == len(str_list[k]):
                num_count[k] += 1
    
    print(tc[0])
    for i in range(len(str_list)):
        for j in range(num_count[i]):
            print(str_list[i],end=' ')

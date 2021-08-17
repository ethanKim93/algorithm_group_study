import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for t in range(T):
    str1 = str(input())
    str2 = str(input())

    N = len(str1)
    M = len(str2)

    for i in range(M-N+1): # str2를 하나하나 보면서
        if str2[i:i+N] == str1: # str2의 i번째부터 str1의 길이 N까지의 str이 일치하는지 확인
            result = 1
            break # str1의 문자를 확인하면 조건문 탈출
        result = 0

    print('#{} {}'.format(t+1,result))
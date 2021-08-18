import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    str1 = input()
    str2 = input()
    counter = 0
    for i in range(len(str2)-len(str1)+1):
        j = 0
        while j != len(str1):
            if str1[j] == str2[i]:
                j += 1
                i += 1
            else:
                break
        if j == len(str1):
            counter = 1
            break
    print('#{} {}'.format(test_case,counter))

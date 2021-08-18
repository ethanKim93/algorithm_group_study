import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    i = 0
    while len(str1)+i <= len(str2):
        if str2[i:len(str1)+i] == str1:
            print('#{} 1'.format(tc))
            break
        i += 1
    else:
        print('#{} 0'.format(tc))

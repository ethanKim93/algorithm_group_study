import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    str1, str2 = input().split()
    counter = 0
    k = len(str1)-len(str2)+1
    i = 0
    word = 0
    while i < k:
        counter = 0
        j = 0
        change_i = i
        while str1[change_i] == str2[j]:
            change_i += 1
            j += 1
            counter += 1
            if counter == len(str2):
                word += 1
                i += len(str2)-1
                break
        i += 1
    answer = len(str1) - word*(len(str2)-1)
    print('#{} {}'.format(test_case, answer))

# slicing 이용

import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def remove_str(s):
    while True:
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2:]
                break
        else:
            return s


for test in range(T):
    result = remove_str(str(input()))
    result_len = len(result)
    print('#{} {}'.format(test + 1, result_len))

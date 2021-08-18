import sys
sys.stdin = open('sample_input.txt')

def find_str (str1, str2):
    f = 0   # str1
    s = 0  # str2
    while f < len(str1) and s < len(str2):
        if str2[s] != str1[f]:
            s = s - f
            f = -1
        s = s + 1
        f = f + 1
    if f == len(str1):
        return 1

    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    print('#{} {}'.format(tc, find_str(str1, str2)))
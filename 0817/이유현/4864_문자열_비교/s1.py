import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    ans = 0

    for i in range(len(str2)-len(str1)):
        if str1 == str2[i:i+len(str1)]:
            ans = 1
            break
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))
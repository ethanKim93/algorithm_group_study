import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    s = input()

    i = 0

    while True:
        if i == len(s)-1:
            break

        elif s[i] == s[i+1]:    # 양 옆 문자가 같으면
            s1 = s[:i]      # s1은 i까지 끊고
            s2 = s[i+2:]    # s2는 i+2부터 끝까지 끊은다음
            s = (s1 + s2)   # 더해서 새로운 문자열 만들기

            i = 0
        else:
            i += 1

    print('#{} {}'.format(tc, len(s)))




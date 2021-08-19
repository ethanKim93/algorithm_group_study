import sys

sys.stdin = open('sample_input.txt')

for tc in range(1, int(input()) + 1):
    string = list(input())
    result = []  # 스택
    i = 0
    while string:  # 비교할 문자열이 남아있지 않으면 종료
        if len(string) > 1 and string[i] == string[i + 1]:  # 반복문자가 있으면 문자열에서 제거
            string.pop(i)
            string.pop(i)
        else:
            if result and result[-1] == string[i]:  # 반복문자가 아니지만 스택과 이어지면 반복문자가 되는경우 스택에서 제거
                string.pop(i)
                result.pop()
            else:
                result.append(string.pop(i))    # 반복문자가 아닌경우 push
            continue
    print('#{} {}'.format(tc, len(result)))

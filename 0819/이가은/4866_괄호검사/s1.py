import sys
sys.stdin = open("sample_input.txt")

def pair(s):                # 괄호 짝 검사하는 함수
    N = len(s)
    result = []

    for i in range(N):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            result.append(s[i])

        elif s[i] == ')':
            if result and result[-1] == '(':    # result = [] 일 때 생기는 인덱스 에러 해결
                result.pop(-1)
            else:
                return 0

        elif s[i] == '}':
            if result and result[-1] == '{':
                result.pop(-1)
            else:
                return 0

        elif s[i] == ']':
            if result and result[-1] == '[':
                result.pop(-1)
            else:
                return 0

    if len(result):
        return 0
    else:
        return 1


T = int(input())

for test in range(T):
    check_str = str(input())
    result = pair(check_str)

    print('#{} {}'.format(test+1, result))

import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    b = input()
    bracket = []

    for i in range(len(b)):
        if b[i] == '(':
            bracket.append('(')

        elif b[i] == ')':
            if not bracket:
                bracket.append(')')
            else:
                if bracket[-1] == '(':
                    bracket.pop()
                else:
                    bracket.append(')')

        elif b[i] == '{':
            bracket.append('{')

        elif b[i] == '}':
            if not bracket:
                bracket.append('}')
            else:
                if bracket[-1] == '{':
                    bracket.pop()
                else:
                    bracket.append('}')

    if not bracket:
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))
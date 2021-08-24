import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1,T+1):
    words = input().split()
    stack = []
    cal = ['+', '-', '*', '/']
    for word in words:
        if word == '.':
            if len(stack) == 1:
                result = stack.pop()
            else:                           # 연산종료되었는데 숫자가 하나 이상 남았다면, 오류로 에러
                result = 'error'
            break
        elif word != '+' and word != '-' and word != '*' and word != '/':
            stack.append(word)
        else:
            if len(stack) > 1:
                a, b = stack.pop(), stack.pop()
                if (a in cal) or (b in cal):            # stack에서 꺼냈는데 숫자가 아닌 연산자가 나온다면 연산불가로 에러
                    result = 'error'
                    break
                else:
                    if word == '+':
                        stack.append(int(a)+int(b))
                    elif word == '-':
                        stack.append(int(b)-int(a))         # -,/ 연산할때 순서 주의
                    elif word == '*':
                        stack.append(int(a)*int(b))
                    elif word == '/':
                        stack.append(int(b)//int(a))        # 항상 나누어떨어진다고 했으므로, '/'로 하면 float로 결과가 나오므로
            else:
                result = 'error'                            # 길이가 1보다 크지 않으면, 숫자가 2개가 없다는 의미이므로 연산불가로 에러
                break
    print('#{} {}'.format(tc, result))

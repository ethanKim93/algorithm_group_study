import sys
sys.stdin = open('sample_input.txt')
for tc in range(1, int(input())+1):
    expression = input().split(' ')
    result = []
    for oper in expression:
        if oper.isdecimal():    # 피연산자는 push
            result.append(oper)
        elif oper == '.':       # .이 입력되었을때 최종 결과만 남아있는게 아니라면 error
            if len(result) == 1:    # 최종결과만 남아있다면 출력
                print('#{} {}'.format(tc, result[0]))
                break
            else:
                print('#{} error'.format(tc))
        else:
            if len(result) < 2: # 연산자일때 피연산자가 2개미만이라면 error
                print('#{} error'.format(tc))
                break
            a = result.pop()
            b = result.pop()
            if oper == '+':
                result.append(int(a)+int(b))
            elif oper == '*':
                result.append(int(a)*int(b))
            elif oper == '-':
                result.append(int(b)-int(a))
            elif oper == '/':
                result.append(int(b)//int(a))
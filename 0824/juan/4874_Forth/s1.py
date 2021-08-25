import sys
sys.stdin = open("sample_input.txt")

def Forth():
    for i in post:                                  # 후위표기식 순회
        if i.isdigit():                             # 피연산자(숫자)인 경우
            stack.append(int(i))                    # 스택에 추가
        elif len(stack) > 1:                        # 피연산자가 아닌 경우(연산자 or '.') 스택의 길이가 2이상이어야 하므로
            b = stack.pop()
            a = stack.pop()
            if i == '+':                            # 사칙연산이면 계산 후 스택에 다시 추가
                stack.append(a+b)
            elif i == '-':
                stack.append(a-b)
            elif i == '*':
                stack.append(a*b)
            elif i == '/':
                stack.append(a/b)
            else:                                   # 스택의 길이가 2이상인데 '.'이 나온 경우 에러
                return 'error'
        elif len(stack) == 1 and i == '.':          # 스택에 요소가 1개이면서 '.'로 끝난 경우에는 스택의 요소 꺼내서 return
            return int(stack[0])
        else:                                       # 스택에 요소가 1개가 아닌데 '.'로 끝난 경우 에러
            return 'error'

T = int(input())

for tc in range(1, T+1):
    post = input().split()                          # 후위표기식 입력
    stack = []                                      # 스택 초기화
    print('#{} {}'.format(tc, Forth()))
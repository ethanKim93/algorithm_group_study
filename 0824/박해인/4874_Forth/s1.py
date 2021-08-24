import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    str = list(input().split())
    stack = []

    for s in str:
        try:
            if s.isdecimal():  # 숫자를 만나면
                stack.append(int(s))  # int로 형변환해서 push
            else:  # 연산자를 만나면
                if s == '+':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2 + num1)  # 후입선출구조 -> num2가 str에서 앞에 있던 숫자
                elif s == '*':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2 * num1)
                elif s == '/':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2 // num1)
                elif s == '-':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2 - num1)
                elif s == '.':  # str이 끝나면
                    if len(stack) == 1:  # stack에 하나만 남아있다면 == 결과 값
                        print('#{} {}'.format(test_case, stack[0]))
                    else:  # stack에 0, 2이상
                        print('#{} error'.format(test_case))
        except:  # 숫자나 연산자를 pop하다가 에러가 났을 경우
            print('#{} error'.format(test_case))
            break

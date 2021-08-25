import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    expression = input().split()
    operation_list = ['+', '-', '*', '/', '.']  # 연산자와. 리스트 생성
    number_stack = []  # 숫자넣을 스택 생성

    for i in expression:
        if i not in operation_list:  # 연산자와.이 아니라면 숫자스택에 삽입
            number_stack.append(int(i))
        else:
            if len(number_stack) > 1 and i == '+':  # 숫자스택이 두개 이상이고 i가 +면 + 연산 수행
                b = number_stack.pop()
                a = number_stack.pop()
                c = a + b
                number_stack.append(c)
            elif len(number_stack) > 1 and i == '-':  # -연산 수행
                b = number_stack.pop()
                a = number_stack.pop()
                c = a - b
                number_stack.append(c)
            elif len(number_stack) > 1 and i == '*':
                b = number_stack.pop()
                a = number_stack.pop()
                c = a * b
                number_stack.append(c)
            elif len(number_stack) > 1 and i == '/':  # 정수로 나타내기위해 // 사용
                b = number_stack.pop()
                a = number_stack.pop()
                c = a // b
                number_stack.append(c)
            elif i == '.':
                if len(number_stack) == 1:
                    print('#{} {}'.format(tc, number_stack[0]))
                else:
                    print('#{} {}'.format(tc, 'error'))
            else:
                print('#{} {}'.format(tc, 'error'))
                break

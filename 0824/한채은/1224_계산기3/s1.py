import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    strings = str(input())
    stack = []
    numbers = []

    icp = {'*': 2, '+': 1, '(': 3}  # 넣을때
    isp = {'*': 2, '+': 1, '(': 0}  # 스택안

    # Step 1: 중위 => 후위 표기법 변경
    for string in strings:
        # 피연산자인 경우: 숫자 리스트 넣기
        if string.isdigit():
            numbers.append(string)

        # 연산자인 경우
        else:
            # stack이 빈 경우 => 무조건 append(여는 괄호의 case)
            if not stack:
                stack.append(string)
                continue

            # stack이 비지 않은 경우
            elif stack:
                # 닫는 괄호인 경우, 여는 괄호가 나올 때 까지 pop
                if string == ')':
                    while stack[-1] != '(':
                        numbers.append(stack.pop())
                    stack.pop()

                # icp & isp 비교
                elif icp[string] > isp[stack[-1]]:
                    stack.append(string)

                else:
                    # icp가 isp 보다 작으면 계속 pop & 연산자 리스트에 append
                    while icp[string] <= isp[stack[-1]]:
                        numbers.append(stack.pop())
                    stack.append(string)

    print(numbers)

    # total = []
    # for i in final:
    #     if i == '+':
    #         a = total.pop()
    #         b = total.pop()
    #         c = int(a) + int(b)
    #         total.append(c)
    #
    #     elif i == '*':
    #         a = total.pop()
    #         b = total.pop()
    #         c = int(a) * int(b)
    #         total.append(c)
    #
    #     else:
    #         total.append(i)
    #
    # print('#{} {}'.format(tc, total[0]))

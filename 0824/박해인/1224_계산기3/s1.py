import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    L = int(input())  # 테스트 케이스의 길이 L
    text = input()

    # 후위 표기식으로 바꾸기
    num = []  # 숫자 담기
    stack = []

    for a in text:
        if a.isdecimal():
            num.append(a)
        else:
            if a == '(':
                stack.append(a)
            elif a == ')':
                while stack[-1] != '(':
                    num.append(stack.pop())
                stack.pop() # 연산 끝난 )는 버리기
            elif a == '*':
                stack.append(a)
            elif a == '+':
                while stack and stack[-1] != '(':
                    num.append(stack.pop())
                stack.append(a)

    while stack:
        num.append(stack.pop())

    for n in num:
        if n.isdecimal():  # 숫자를 만나면
            stack.append(int(n))  # int로 형변환해서 push
        else:  # 연산자를 만나면
            if n == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 + num1)  # 후입선출구조 -> num2가 str에서 앞에 있던 숫자
            elif n == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 * num1)


    print('#{} {}'.format(test_case, stack[0]))

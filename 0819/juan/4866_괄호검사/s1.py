import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    text = input()
    stack = []                                  # stack 초기화

    for i in text:
        if i == '(' or i == '{':                # 문자열 중 열린 괄호 인 경우 stack에 추가
            stack.append(i)
        elif i == ')':                          # 닫힌 소괄호인 경우
            if stack and stack[-1] == '(':      # stack이 채워진 상태이고 짝인 맞는 경우 stack에서 꺼냄
                stack.pop()
            else:
                stack.append(i)                 # stack 비었거나 짝이 맞지 않으면 stack에 추가(이 소괄호는 stack 계속 남아있음)
        elif i == '}':                          # 닫힌 중괄호인 경우
            if stack and stack[-1] == '{':      # stack이 채워진 상태이고 짝인 맞는 경우 stack에서 꺼냄
                stack.pop()
            else:
                stack.append(i)                 # stack 비었거나 짝이 맞지 않으면 stack에 추가(이 중괄호는 stack 계속 남아있음)

    result = 0 if stack else 1                  # 문자열을 모두 순회한 후에 stack이 채워진 상태면 짝이 맞지 않았던 것이므로 0, 비었으면 1을 변수에 할당 후 출력
    print('#{} {}'.format(tc, result))


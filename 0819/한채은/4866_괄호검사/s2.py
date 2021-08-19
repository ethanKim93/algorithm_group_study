for tc in range(1, T+1):
    text = input()
    stack = []
    for i in text:
        if i == '(' or i == '{':
            stack.append(i)

        elif i == ')':  # 닫힌 괄호가 들어왔는데
            if stack and stack[-1] == '(':      # 스택이 비어있지않고, 마지막이 열린 소괄호면
                stack.pop()         # 빼버리기
            else:
                break

        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                break

    result = 0 if stack else 1
    print('#{} {}'.format(tc, result)
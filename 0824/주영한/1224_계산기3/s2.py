import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = input()     # 더미 값
    eq = input()
    post, stack = [], []    # post는 후위표기식 스택, stack은 연산자가 들어갈 스택이다.
    for token in eq:
        if token.isdecimal():   # 숫자이면 post에 추가한다.
            post.append(token)
        else:
            if token == "(":        # "("의 icp는 3이므로, 무조건 넣어준다.
                stack.append(token)
            elif token == "*":
                while stack and stack[-1] == "*":
                    # "*"의 icp와 isp는 2이므로, 이보다 우선순위가 높은 모든 연산자를
                    # 빼준다. isp가 2보다 큰 연산자는 없으므로, 다른 *을 만날때 까지 빼준다.
                    post.append(stack.pop())
                stack.append(token)
            elif token == "+":
                while stack and stack[-1] != "(":
                    # "+"의 icp와 isp는 1이므로, 이보다 우선순위가 높은 모든 연산자를
                    # 빼준다. "("의 isp는 0이므로, "("을 만나면 반복을 중단한다.
                    post.append(stack.pop())
                stack.append(token)
            else:
                while stack and stack[-1] != "(":
                    # ")"의 icp와 isp는 0이므로, 이보다 우선순위가 높은 모든 연산자를
                    # 빼준다. "("의 isp는 0이므로, "("을 만나면 반복을 중단한다.
                    # 이후 stack안에 있는 "("를 제거한다.
                    post.append(stack.pop())
                stack.pop()
    while stack:
        post.append(stack.pop())

    for token in post:
        if token.isdecimal():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            else:
                stack.append(a * b)
    print("#{} {}".format(tc, *stack))
# 모르겠어요.............

parenthesis = input()
stack = []

for p in parenthesis:
    if p == '(' or '{' or '[':
        stack.append(p)
    else:  # 괄호만 들어온다고 가정하고 else 사용
        stack.pop(-1)
        if
def postfix(texts):
    post = []
    operation = []
    operator = "*+"
    isp = { "*" : 2, "+" : 1}
    icp = { "*" : 2, "+" : 1}
    for text in texts:
        if text in operator:
            if not post:
                # 스택에 아무 요소가 없을 경우는 추가해준다.
                post.append(text)
                continue

            # 낮은 연산자를 만날때 까지 pop하고, 큰 연산자일 경우 스택에 추가해준다.
            while len(post) > 0 and icp[text] <= isp[post[-1]]:
                operation.append(post.pop())
            post.append(text)
        else:
            # 피 연산자의 경우 출력한다.
            operation.append(int(text))
    operation.extend(post[::-1])
    return operation

def postfix_operation(operation):
    idx = 0
    while len(operation) > 1:
        if operation[idx] == "*":
            operation[idx - 2] = operation[idx - 2] * operation[idx - 1]
            operation.pop(idx - 1)
            operation.pop(idx - 1)
            idx -= 1
        elif operation[idx] == "+":
            operation[idx - 2] = operation[idx - 2] + operation[idx - 1]
            operation.pop(idx - 1)
            operation.pop(idx - 1)
            idx -= 1
        else:
            idx += 1
    return operation[0]

for tc in range(1, 11):
    dum = input()
    print("#{} {}".format(tc, postfix_operation(postfix(input()))))
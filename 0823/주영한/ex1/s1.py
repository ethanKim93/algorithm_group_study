def postfix(texts):
    post = []
    operator = "()*/+-"
    isp = { ")" : 0, "*" : 2, "/" : 2, "+" : 1, "-" : 1, "(" : 0 }
    icp = { ")" : 0, "*" : 2, "/" : 2, "+" : 1, "-" : 1, "(" : 3 }
    for text in texts:
        if text in operator:
            if not post:
                # 스택에 아무 요소가 없을 경우는 추가해준다.
                post.append(text)
                continue

            if text == ")":
                while post[-1] != "(":
                    print(post.pop(), end="")
                post.pop()
                continue

            # 낮은 연산자를 만날때 까지 pop하고, 큰 연산자일 경우 스택에 추가해준다.
            while icp[text] <= isp[post[-1]]:
                print(post.pop(), end="")
            post.append(text)
        else:
            # 피 연산자의 경우 출력한다.
            print(text, end="")
    print()


postfix("(1+(6+5)*(2-8)/2+2)")
postfix("(6+5*(2-8)/2)")
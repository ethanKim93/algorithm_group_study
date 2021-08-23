import sys
sys.stdin = open("input.txt")
for tc in range(1, 2):
    N = int(input())
    exp = list(input())

    stack = []
    res = []
    for i in exp:
        if '0' <= i <= '9':
            res.append(i)

        elif i == '+':
            if len(stack) == 0:
                stack.append(i)
            else: #안비어있을떄
                if stack[-1] == '+': # + 맨뒤 붙었을때
                    stack.append(i)
                else: #* 일때 스택 + 나오기 전까지 다 뺌
                    if len(stack) != 0:
                        while stack[-1] != '+':
                            # print(stack.pop())
                            res.append(stack.pop())
        else: #i:* 일때
            if len(stack) == 0:
                stack.append(i)
            else:
                if stack[-1] == '+':
                    stack.append(i)
                else:
                    if len(stack) != 0:
                        while stack[-1] != '+':
                            # print(stack.pop())
                            res.append(stack.pop())
    print(res)
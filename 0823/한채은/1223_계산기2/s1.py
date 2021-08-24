import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):    # tc 10개
    N = int(input())   # tc 길이
    text = input()  # 들어오는 식
    stack = []     # *, +
    final = []    # 최종 쌓는 식

    for op in text:
        if op == '*':   # 곱하기 나오면
            stack.append(op)    # 스택에 쌓기

        elif op == '+':  # 플러스 나오면
            if len(stack) == 0:  # 스택이 비었으면
                stack.append(op)    # 플러스 쌓기
            else:
                while stack:    # 스택에 뭐가 있으면 스택 빌때까지
                    final.append(stack.pop())   # 새로 만드는 식에 스택에 쌓여있는 연산자 뒤에서부터 넣어주기
                stack.append(op)    # 스택에 플러스 추가
        else:   # 숫자 나오면
            final.append(op)  # 바로 숫자 쌓기

    while stack:
        final.append(stack.pop())   # 스택에 남아있는거 털기

    print(final)

    # 계산
    total = []
    for i in final:
        if i == '+':    # 피연산자 2개가 나오고 연산자가 나오니까
            a = total.pop()     # 스택에서 2개 빼고
            b = total.pop()
            c = int(a) + int(b)
            total.append(c)     # 다시 올려놓기

        elif i == '*':
            a = total.pop()
            b = total.pop()
            c = int(a) * int(b)
            total.append(c)

        else:   # 피연산자는 모두 올리기
            total.append(i)

    print('#{} {}'.format(tc, *total))


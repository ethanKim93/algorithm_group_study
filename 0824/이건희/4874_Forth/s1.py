import sys

sys.stdin = open("input.txt")
t = int(input())
for tc in range(1, t + 1):
    maps = input().split()
    stack = []
    ans = 0
    for i in maps:
        if i.isdigit():  # 숫자일 때
            stack.append(int(i))
        else:  # 숫자가 아닐 때
            if i != "." and len(stack) < 2:  # .이 아니고, 숫자가 2개 미만이라면
                print("#{} {}".format(tc, "error"))  # 오류 출력
                break
            # 연산
            elif i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(second // first)
            # .이 들어왔을 때
            else:
                if len(stack) >= 2:  # .이 들어왔는데 숫자가 2개 이상이면 오류 출력
                    print("#{} {}".format(tc, "error"))
                else:  # 1개면 stack출력
                    print("#{} {}".format(tc, int(stack[-1])))

import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t + 1):
    temps = []
    ans = 1
    text = list(input())
    for i in text:
        if i == "(":
            temps.append(i)
        elif i == ")":
            if not temps: # 뺄 값이 없을 경우
                ans = 0
                break

            elif temps.pop() != "(": # 뺀 값이 '('이 아닐 경우
                ans = 0
                break
        elif i == "{":
            temps.append(i)
        elif i == "}":
            if not temps: # 뺄 값이 없을 경우
                ans = 0
                break

            elif temps.pop() != "{": # 뺸 값이 '{'이 아닐 경우
                ans = 0
                break


    if temps:
        ans = 0

    print("#{} {}".format(tc, ans))
import sys
sys.stdin = open("sample_input.txt")

brackets = "{}()"
brackets_right = {"{" : "}", "(" : ")"}
brackets_wrong = {"{" : ")", "(" : "}"}

T = int(input())
for tc in range(1, T + 1):
    texts = input()
    check_stack = []
    for text in texts:
        if text in brackets:
            if not check_stack:
                check_stack.append(text)
                continue
            if brackets_right[check_stack[-1]] == text:
                check_stack.pop(-1)
                continue
            else:
                if brackets_wrong[check_stack[-1]] == text:
                    break
                check_stack.append(text)
    result = 0 if len(check_stack) else 1
    print("#{} {}".format(tc, result))
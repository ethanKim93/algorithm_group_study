import sys

sys.stdin = open('sample_input.txt')

for tc in range(1, int(input())+1):
    string = input()
    arr = []
    answer = 1
    for char in string:
        if char == '{' or char == '(':
            arr.append(char)
        elif char == ')':
            if arr and arr[-1] == '(':
                arr.pop()
            else:
                arr.append(char)
                break
        elif char == '}':
            if arr and arr[-1] == '{':
                arr.pop()
            else:
                arr.append(char)
                break

    answer = 0 if arr else 1
    print('#{} {}'.format(tc, answer))


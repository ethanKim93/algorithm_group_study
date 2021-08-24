exp = input().split()
stack = []
result = ''
for char in exp:
    if char.isdigit():
        result += char
    else:
        stack.append(char)

n = len(stack)
for i in range(n):
    result += stack.pop()

print(' '.join(result))
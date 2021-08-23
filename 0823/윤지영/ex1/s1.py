words = input().split()
stack = []
result = []
for word in words:
    if word == '*' or word == '/' or word == '+' or word == '-' :
        stack.append(word)
    else:
        result.append(word)
while stack:
    result.append(stack.pop())
print(' '.join(map(str, result)))


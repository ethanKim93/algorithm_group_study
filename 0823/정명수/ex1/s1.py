file = input()
number=['0','1','2','3','4','5','6','7','8','9']
answer = []
stack = []
for i in file:
    if i in number:
        answer.append(i)
    else:
        stack.append(i)
while stack:
    answer.append(stack.pop())
print(*answer)

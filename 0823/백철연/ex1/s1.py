
lis = ['2','+','3','*','4','/','5']
re = []
stack = []
operator =['*','/','+','-']

for i in lis:
    if i not in operator:
        re.append(i)
    if i in operator:
        stack.append(i)
for j in stack:
    re.append(stack.pop())
while stack:
    re += stack.pop()
print(' '.join(re))

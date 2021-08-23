file = input()
num = ['0','1','2','3','4','5','6','7','8','9']
stack = []
for i in file:
    if i in num:
        print(i, end=' ')
    else:
        stack.append(i)
print(*stack[::-1])

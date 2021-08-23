str1 = '2 + 3 * 4 / 5'
str1_lst = list(str1.split())
stk = []

for s in range(len(str1_lst)):
    if str1_lst[s] == '+' or str1_lst[s] == '-' or str1_lst[s] == '*' or str1_lst[s] == '/':
        stk.append(str1_lst[s])
    else:
        print(str1_lst[s], end=' ')
while stk:
    print(stk.pop(), end=' ')
print()

# step2
str1 = '2 + 3 * 4 / 5'
str1_lst = list(str1.split())
calc = []
stk = []

for s in range(len(str1_lst)):
    if str1_lst[s] == '+' or str1_lst[s] == '-' or str1_lst[s] == '*' or str1_lst[s] == '/':
        stk.append(str1_lst[s])
    else:
        calc.append(str1_lst[s])
while stk:
    calc.append(stk.pop())

stk2 = []
for c in range(len(calc)):
    if calc[c] == '+':
        a = stk2.pop()
        b = stk2.pop()
        res = b + a
        stk2.append(res)
    elif calc[c] == '-':
        a = stk2.pop()
        b = stk2.pop()
        res = b - a
        stk2.append(res)
    elif calc[c] == '*':
        a = stk2.pop()
        b = stk2.pop()
        res = b * a
        stk2.append(res)
    elif calc[c] == '/':
        a = stk2.pop()
        b = stk2.pop()
        res = b / a
        stk2.append(res)
    else:
        stk2.append(int(calc[c]))
print(stk2.pop())

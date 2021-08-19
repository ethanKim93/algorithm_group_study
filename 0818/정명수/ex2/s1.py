def push(item):
    li.append(item)
def pop():
    if len(li) == 0:
        return
    else:
        return li.pop(-1)
li=[]
case = input()
for i in case:
    if i == '(':
        push(i)
    if i == ')':
        pop()
print(li)
def push(a):
    s.append(a)
def pop():
    if len(s)==0:
        return
    else:
        return s.pop(-1)

s=[]
push('김밥')
push('떡볶이')
push('순대')
print(pop())
print(pop())

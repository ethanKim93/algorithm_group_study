def push(item):
    li.append(item)
def pop():
    if len(li) == 0:
        return
    else:
        return li.pop(-1)
li=[]
push(1)         #[1]
push(2)         #[1,2]
push(3)         #[1,2,3]
pop()           #[1,2]
pop()           #[1]
pop()           #[]
print(li)

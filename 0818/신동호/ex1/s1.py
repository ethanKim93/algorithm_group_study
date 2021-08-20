# 리스트에 append로 stack 구현
stack1 = []
stack1.append(1)
stack1.append(2)
stack1.append(3)
while stack1:
    print(stack1.pop())

# push, pop을 push, pull 함수로 구현
top = -1
s = [0]*10
def push(num):
    global top
    while top < 10 - 1:
        top += 1
        s[top] = num
        return
    else:
        return

def pull():
    global top
    while top >= 0:
        top -= 1
        print(s[top+1])
        s[top+1] = 0
        return
    else:
        return

for i in range(10):
    push(i)

for j in range(10):
    pull()
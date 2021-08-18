class Stack:
    # 리스트를 이용하여 스택 생성
    def __init__(self):
        self.stack = []

    # PUSH
    def push(self, item):
        self.stack.append(item)

    # POP
    def pop(self):
        if self.isEmpty():
            return
        else:
            return self.stack.pop()

    # 스택에서 top의 값 읽어오기
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None

    # 스택이 비어있는지 확인
    def isEmpty(self):
        return len(self.stack) == 0


s1 = Stack()
for i in range(3):
    s1.push(i)

print(s1.stack)

for _ in range(3):
    print(s1.pop())
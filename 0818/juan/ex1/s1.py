class Stack:
    # 생성자
    def __init__(self):
        self.data = []

    # stack이 비어있는지 확인
    def is_empty(self):
        return False if self.data else True

    # stack에 push
    def push(self, item):
        self.data.append(item)

    # stack에서 pop
    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            return None

    # 출력
    def __str__(self):
        result = '\n-----'
        for d in self.data:
            result = '\n| {} |'.format(d) + result
        return result


s = Stack()
print(s.is_empty())  # True

s.push(1)
print(s)
s.push(2)
print(s)
s.push(3)
print(s)
print(s.is_empty())  # False

print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.is_empty())  # True
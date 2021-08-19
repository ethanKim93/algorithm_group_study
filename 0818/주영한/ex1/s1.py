class stack:
    def __init__(self, length = None):
        self.top = -1
        if length:
            self.length = length
            self.data = [0] * length
        else :    
            self.length = 0
            self.data = []

    def push(self, item):
        # 데이터가 미리 잡혀 있지 않을 경우에는 append를 통해 추가한다.
        if self.top >= self.length - 1:
            self.top += 1
            self.length += 1
            self.data.append(item)
        # 데이터가 미리 잡혀 있을 경우에는 인덱싱으로 추가한다.
        else:
            self.top += 1
            self.data[self.top] = item
    
    def pop(self):
        if self.top == -1:
            return None
        result = self.data.pop(self.top)
        self.top -= 1
        return result

    def isempty(self):
        if self.top == -1:
            return True
        return False

    def __str__(self):
        return " ".join(map(str, self.data[:self.top + 1]))

# 스택의 사이즈를 선언해줄 수 있다.
a = stack(10)
print(a)
a.push(10)      #[10]
a.push(2)       #[10, 2]
a.push(3)       #[10, 2, 3]
a.push(4)       #[10, 2, 3, 4]
print(a)
print(a.isempty())
print(a.pop())  #[10, 2, 3] / 4
print(a.pop())  #[10, 2] / 3
print(a.pop())  #[10] / 2
print(a.pop())  #[] / 10
print(a.isempty())

# 스택의 사이즈를 선언하지 않아도 된다.
b = stack()
print(b)
print(b.pop())
print(b.isempty())
b.push(10)
b.push(2)
print(b)
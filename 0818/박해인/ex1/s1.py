class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
                # underflow <-> overflow
                return '제거할 원소가 없습니다.'
        else:
                return self.items.pop(-1)

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if len(self.items) == 0:
            return '반환할 원소가 없습니다.'
        return self.items[-1]


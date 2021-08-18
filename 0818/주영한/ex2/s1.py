import sys


class stack:
    def __init__(self, input_list=None, length=None):
        self.top_idx = -1
        if input_list:
            self.length = len(input_list)
            self.top_idx = len(input_list) - 1
            self.data = input_list
        elif length:
            self.length = length
            self.data = [0] * length
        else:
            self.length = 0
            self.data = []

    def push(self, item):
        if self.top_idx >= self.length - 1:
            self.top_idx += 1
            self.length += 1
            self.data.append(item)
        else:
            self.top_idx += 1
            self.data[self.top_idx] = item

    def top(self):
        return self.data[self.top_idx]

    def pop(self):
        if self.top_idx == -1:
            return None
        result = self.data.pop(self.top_idx)
        self.length -= 1
        self.top_idx -= 1
        return result

    def isempty(self):
        if self.top_idx == -1:
            return True
        return False

    def __str__(self):
        return "".join(map(str, self.data[:self.top_idx + 1]))
# -----------------------------------------------------------------

def check(brackets, brackets_stack):
    while len(brackets):
        if brackets_stack.isempty():
            brackets_stack.push((brackets.pop(0)))
            continue
        temp = brackets.pop(0)
        if brackets_stack.top() == temp:
            brackets_stack.push(temp)
        else:
            brackets_stack.pop()
    if not brackets_stack.isempty():
        return False
    return True



sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    brackets = list(input())
    brackets_stack = stack()
    print("#{} {}".format(tc, check(brackets, brackets_stack)))

import sys
sys.stdin = open("input.txt")


class Stack:
    def __init__(self, cnt):
        self.li = [0] * cnt
        self.i = -1

    def push(self, ch):
        self.i += 1
        self.li[self.i] = ch

    def pop(self):
        ch = self.li[self.i]
        self.li[self.i] = 0
        self.i -= 1
        return ch


for _ in range(2):
    st = input()
    s = Stack(len(st))
    for c in st:
        try:
            if c == "(":
                s.push("(")
            else:
                s.pop()
        except:
            print(False)
    else:
        if s.li[0] != 0:
            print(False)
        else:
            print(True)

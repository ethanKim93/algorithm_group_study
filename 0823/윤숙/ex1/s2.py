"""
이해가 안가서 s1의 코드로 공부하여 짰습니다.

"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

def infix_to_postfix(arr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    operand = Stack()
    stack = []
    token_list = arr.split()


    for token in token_list:
        if token == '(':
            operand.push(token)

        elif token == ')':
            toptoken = operand.pop()
            while toptoken != '(':
                stack.append(toptoken)
                toptoken = operand.pop()

        elif token in '+-/*^':
            while (not operand.isEmpty()) and (
                    prec[operand.top()] >= prec[token]):
                stack.append(operand.pop())
            operand.push(token)

        else:
            stack.append(token)

    while not operand.isEmpty():
        stack.append(operand.pop())
    return " ".join(stack)




arr = input()
result = infix_to_postfix(arr)
print(result)

# infix -> postfix 방법
# 1. 연산자 우선순위에 따라 괄호를 삽입한다. ->연산자마다 괄호한쌍씩 할당
# 2. 연산자를 자신의 괄호 쌍중에서 오른쪽 괄호의 오른쪽으로 이동
# 3. 괄호를 모두 지운다.
# 연산자 우선순위 * / + -
# A+B*C -> ABC *+
# 1. 피연산자의 순서는 그대로 유지
# 2. 수식의 왼쪽부터 고려하기 때문에 +를 *보다 먼저 고려한다.
# 3. +의 위치는 다음에 만나는 연산자 (여기선 *)에 의해 결정된다.
# 4. *이 +보다 연산순위가 높기 때문에 *다음에 +가 위치해야한다. -> 우선순위가 높은 연산자 부터 차례대호 나열

# (A+B)*C-> AB+C*
# 1. +는 *보다 먼저 )를 만나기 때문에 )다음에 위치
# 2. )의 우선 순위가 *보다 높기 때문에 +연산자는 ) 다음에 위치


# 피연산자는 그대로!
# 뒤에나오는 다음 순서의 연산자를 보고 바꿔준다.

'''
Infix to postfix
'''


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


def infix_to_postfix(infix):
    prec = {}  # 연산자 딕셔너리를 만들어서 우선순위 매기기
    prec["*"] = 3  # {'*':3} 과 같은 말
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opstack = Stack()  # 연산자를 쌓을 스택 공간을 만들어주기
    outstack = []  # postfix 결과를 쌓을 list 공간
    token_list = infix.split()
    # 입력은 스페이스바로 하나하나 띄워서 받으니까 split()을 통해 각 인덱스에 문자 하나씩 넣기

    for token in token_list:
        if token == '(':
            opstack.push(token)

        elif token == ')':  # 오른쪽 괄호가 나타나면
            toptoken = opstack.pop()  # 맨 위에 있는 토큰을 toptoken이라 한다
            while toptoken != '(':  # 왼쪽괄호를 만나기 전까지
                outstack.append(toptoken)  # 만나는 모든 토큰을 outstack리스트에 저장한다
                toptoken = opstack.pop()  # toptoken 값 바꾸기

        elif token in '+-/*^':  # 연산자를 만나면
            while (not opstack.isEmpty()) and (
                    prec[opstack.top()] >= prec[token]):  # 연산 순위와, opstack내에 무언가가 존재한다는 전제 하에
                outstack.append(opstack.pop())
            opstack.push(token)  # 연산자 우선순위에 따라 토큰 붙인다

        else:  # 피연산자는 그냥 붙이면 된다
            outstack.append(token)

    while not opstack.isEmpty():  # 연산자 스택이 빌 때까지
        outstack.append(opstack.pop())  # 연산자 다뽑아버리기
    return " ".join(outstack)  # 입력 형태랑 똑같이 만들어서 출력하기


"""
1 + ( 2 + 3 ) / 4
1 2 3 + 4 / +
"""
infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)

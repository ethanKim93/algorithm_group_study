import sys
sys.stdin = open('input.txt')
def isp(oper):      # 스택내에 있을때의 우선순위
    if oper == '(':
        return 0
    elif oper == '*':
        return 2
    elif oper == '+':
        return 1

def icp(oper):      # token일때의 우선순위
    if oper == '(':
        return 3
    elif oper == '*':
        return 2
    elif oper == '+':
        return 1

def postfix():
    for token in expression:
        if token.isdecimal():    # 토큰이 피연산자면 결과에 push
            result.append(token)
        elif token == ')':       # 토큰이 닫는괄호라면 여는 괄호를 만날 때 까지 모두 pop해서 결과에 push
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()          # 여는 괄호는 삭제
        else:                    # 토큰이 여는괄호 or * or + 일때
            if stack and icp(token) > isp(stack[-1]): # 우선순위가 스택 top보다 높을 때 스택에 push
                stack.append(token)
            elif not stack:
                stack.append(token)
            else:                # 토큰의 우선순위가 스택 top의 우선순위 보다 같거나 낮으면
                while stack and icp(token) <= isp(stack[-1]):   # 스택 top의 우선순위가 낮아질때 까지 pop하고 결과에 push
                    result.append(stack.pop())
                stack.append(token) # 스택에 push
    while stack:    # 스택에 남아있는 모든 연산자들을 pop 해서 결과에 push
        result.append(stack.pop())

def postfix_calc():             # 후위표기식 계산 함수
    for token in result:
        if token.isdecimal():   # 피연산자라면 push
            answer.append(int(token))
        else:                   # 연산자라면 스택에서 피연산자 둘을 꺼내와서 계산 후 push
            a = answer.pop()
            b = answer.pop()
            if token == '+':    # +일떄
                answer.append(a+b)
            else:               # *일때
                answer.append(a*b)
    return answer[0]            # 스택에 남아있는 정수(최종 결과) return


for tc in range(1, 11):
    N = int(input())
    expression = list(input())
    stack = []  # 스택
    result = [] # 변환결과 배열
    answer = [] # 계산 결과를 담을 배열
    postfix()   # 후위표기식 변환 함수
    print('#{} {}'.format(tc, postfix_calc()))
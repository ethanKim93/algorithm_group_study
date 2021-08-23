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

Q = ['2', '+', '3', '*', '4', '/', '5']

stack = []
op = []
outstack = []

for i in Q:
    if i == '*' or i == '-' or i == '/' or i == '+':
        op.append(i)
print(op)

for i in range(len(op)):

    if op[i] == '+' and (op[i + 1] == '*' or op[i + 1] == '/'):
        outstack.append(op[i + 1])
        outstack.append(op[i])
    elif op[i] == '-' and (op[i + 1] == '*' or op[i + 1] == '/'):
        outstack.append(op[i + 1])
        outstack.append(op[i])

print(outstack)

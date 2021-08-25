import sys
sys.stdin = open('input.txt')

icp = {'+': 1, '*': 2, '(': 3}
isp = {'+': 1, '*': 2, '(': 0}

for tc in range(1, 11):
    N = int(input())
    raw_exp = list(input())

    # 중위 => 후위
    exp = []
    operator = []
    idx = 0
    while idx < N:
        if raw_exp[idx].isdigit():
            exp.append(raw_exp[idx])
            idx += 1
        elif raw_exp[idx] == ')':
            temp = operator.pop()
            if temp == '(':
                idx += 1
            else:
                exp.append(temp)
        else:
            if operator:
                if icp[raw_exp[idx]] > isp[operator[-1]]:
                    operator.append(raw_exp[idx])
                    idx += 1
                else:
                    exp.append(operator.pop())
            else:
                operator.append(raw_exp[idx])
                idx += 1
    while operator:
        exp.append(operator.pop())

    # 후위표기법 계산
    result = []
    for char in exp:
        if char.isdigit():
            result.append(int(char))
        else:
            if char == '+':
                result.append(result.pop() + result.pop())
            else:
                result.append(result.pop() * result.pop())
    print('#{} {}'.format(tc, result[0]))

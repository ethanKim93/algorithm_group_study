import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    cal = list(map(str, input()))

    stack = []  # 연산자 저장스택
    num = ''  # 숫자 저장 문자열
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in cal:  # 계산식안에서 한개씩 뽑는다.
        if i in nums:  # 숫자에 해당하면 숫자 저장 문자열에 추가
            num += i
        elif i == '*':  # 곱셈이라면 바로 추가( 우선순위가 +보다 높기떄문)
            stack.append(i)
        else:  # 남은건 +이므로 조건에 맞춰 추가
            while stack:
                num += stack.pop()
            stack.append(i)
    while stack:
        num += stack.pop()

    ans = []
    for j in num:
        if j == '+':
            u = ans.pop()
            v = ans.pop()
            w = u + v
            ans.append(w)
        elif j == '*':
            u = ans.pop()
            v = ans.pop()
            w = u * v
            ans.append(w)
        else:  # 숫자면 정수 타입으로 추가
            ans.append(int(j))

    print('#{} {}'.format(tc, *ans))

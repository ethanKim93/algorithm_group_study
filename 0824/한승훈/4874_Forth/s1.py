import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    lst = list(map(str, input().split()))
    cal = ['+', '-', '/', '*']
    stack = []
    ans = 0
    try:
        for i in lst:
            if i in cal:  # 연산자에 해당하는가?
                v = stack.pop()  # -1부분
                u = stack.pop()  # -2부분
                if i == '+':
                    stack.append(u + v)
                elif i == '-':
                    stack.append(u - v)
                elif i == '*':
                    stack.append(u * v)
                elif i == '/':
                    stack.append(u // v)  # / : 불합격 // : 합격
            elif i == '.':  # 마침표인가?
                if len(stack) == 1:
                    ans = stack.pop()
                else:
                    ans = 'error'
                break
            else:  # 숫자인가?
                stack.append(int(i))  # 리스트에 담은 것은 문자열이기 때문에 정수형으로 교환
    except:
        ans = 'error'

    print('#{} {}'.format(tc, ans))


import sys

sys.stdin = open('input.txt')


def post_order(n):  # 후위 순회를 통해 후위표기식 만들기
    if n:
        post_order(left[n])
        post_order(right[n])
        postfix.append(tree[n])


def postfix_calc():  # 후위표기식 계산 함수
    for token in postfix:
        if token.isdecimal():  # 피연산자라면 push
            result.append(int(token))
        else:  # 연산자라면 스택에서 피연산자 둘을 꺼내와서 계산 후 push
            a = result.pop()
            b = result.pop()
            if token == '+':  # + 일떄
                result.append(a + b)
            elif token == '-':  # - 일때
                result.append(b - a)
            elif token == '/':  # / 일때
                result.append(b / a)
            else:  # * 일때
                result.append(a * b)
    return int(result[0])  # 스택에 남아있는 값 정수형으로 변환 후 return


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)  # 트리
    left = [0] * (N + 1)  # 왼쪽
    right = [0] * (N + 1)  # 오른쪽
    postfix = []  # 후위표기식
    result = []  # 계산 결과를 담을 배열

    for _ in range(N):
        string = input().split(' ')
        if not string[1].isdecimal():  # 연산자가 있는 경우
            idx = int(string[0])
            tree[idx] = string[1]  # 노드에 연산자 입력
            left[idx] = int(string[2])  # 자식노드 입력
            right[idx] = int(string[3])
        else:  # 피연산자인 경우
            idx = int(string[0])  # 노드에 피연산자 입력
            val = string[1]
            tree[idx] = val

    post_order(1)  # 후위표기식 변환
    print('#{} {}'.format(tc, postfix_calc()))  # 후위표기식 계산

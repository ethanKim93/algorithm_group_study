import sys
sys.stdin = open("sample_input.txt")

def postfix(operations):
    operator = "+-*/"

    result = []
    while operations:

        # 확인하는 값을 token으로, 결과값이 들어갈 스택의 top 인덱스를 result_top으로 저장한다.
        token = operations[0]
        result_top = len(result) - 1

        # 토큰이 연산자일 경우, result에 들어가있는 요소 중 top과 그 아래에 있는 요소에 대한 연산을 실시한다.
        # 연산이 완료한 후 토큰은 필요 없으므로 이를 operations 리스트에서 제거한다.
        if token in operator:
            if len(result) < 2:
                return "error"
            if token == "+":
                result[result_top - 1] = result[result_top - 1] + result[result_top]
                del(result[result_top])
            elif token == "-":
                result[result_top - 1] = result[result_top - 1] - result[result_top]
                del(result[result_top])
            elif token == "*":
                result[result_top - 1] = result[result_top - 1] * result[result_top]
                del(result[result_top])
            else :
                result[result_top - 1] = result[result_top - 1] / result[result_top]
                del(result[result_top])
            del(operations[0])

        # 토큰이 . 일 경우, 연산이 종료된 것이기 때문에 result에 있는 값을 확인한다.
        # 만약 result 리스트의 길이가 1이 아니라면 error를 반환한다.
        elif token == ".":
            if len(operations) != 1 or len(result) != 1:
                return "error"
            return int(result[0])

        # 토큰이 피연산자의 경우 result 스택에 요소를 추가한다.
        else :
            result.append(int(token))
            del(operations[0])

    return "error"


T = int(input())

for tc in range(1, T + 1):
    operations = input().split()
    print("#{} {}".format(tc, postfix(operations)))
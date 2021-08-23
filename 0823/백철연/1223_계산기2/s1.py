import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1,T+1):

    N = int(input())
    Cal = input()
#  중위 표기법에서 후위표기법으로 변환
    Cal_int = ''
    Cal_temp = []
    for str in Cal:
        if str == '*':
            Cal_temp.append(str)
        elif str == '+':
            while Cal_temp:
                Cal_int += Cal_temp.pop()
            Cal_temp.append(str)
        else:
            Cal_int += str
    # print(num_int)
    while Cal_temp:              # 마지막 연산자를 넣음
        Cal_int += Cal_temp.pop()
    print(Cal_int)

    result = []
    for str in Cal_int:

        if str == '*':
            mul2 = result.pop()
            mul1 = result.pop()
            mul3 = mul1 * mul2
            result.append(mul3)

        elif str == '+':
            plu2 = result.pop()
            plu1 = result.pop()
            plu3 = plu1 + plu2
            result.append(plu3)

        else:
            result.append(int(str))
    print("#{} {}".format(tc, result[0]))




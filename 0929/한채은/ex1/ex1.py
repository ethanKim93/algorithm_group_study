import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    a = int(input(), 2)
    print(a)


    # int() 함수의 2번째 인자는 디폴트값이 10이기 때문에 생략했을 경우 10진수의 문자열이 숫자로 변환되는 것입니다.
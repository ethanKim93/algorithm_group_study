import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    pipe = input()

    start = end = cnt = 0
    for p in range(len(pipe)):
        if pipe[p] == "(":
            start += 1
        elif pipe[p] == ")":
            start -= 1
            if pipe[p-1] == "(":
                cnt += start
            else:
                cnt += 1
    print('#{} {}'.format(tc, cnt))



'''
stack 을 이용하자
여는 괄호 ( 면 추가
닫힌 괄호: 하나를 pop, 직전의 녀석을 확인을 해서 열린괄호 ( 면 레이저라는 의미
--> 절단을 한 것이기 때문에 내가 가지고 있는 스택의 길이만큼 막대기가 생겼다
    잘려진 막대기를 더해나간다
직전 괄호를 확인했는데 닫힌괄호 ) 라면 쇠막대기의 끝
--> 닫힌 막대기 1을 더해준다
스택에 남아있다는 것은 아직 막대기가 계속된다
'''
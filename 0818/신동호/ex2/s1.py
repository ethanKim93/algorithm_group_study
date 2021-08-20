import sys
sys.stdin = open('input.txt')

def check(words):
    top = -1
    s = [0] * 30 # 최대 스택 30개
    for word in words:
        if word == '(': # top의 위치 1 증가, ( 채워주기
            top += 1
            s[top] = '('
        elif word == ')': # top의 위치 1 감소, ( 빼기
            top -= 1
            if top < -1: # )가 (보다 많음
                return False
            s[top+1] = 0
    if s[top] == '(': # 남아있는 (가 있을 때
        return False
    return True

T = 2

for tc in range(1, T+1):
    print(check(input()))

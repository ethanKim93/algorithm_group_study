import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    li = input()
    li_1 = ' '.join(li.split('()'))  # 레이저'()'를 기준으로 구분
    N = len(li_1)
    pole = cnt = 0   # 막대수 pole , 잘린 막대기 수 cnt 초기화
    for i in range(N):
        if li_1[i] == ' ':    # 공백이면 레이저쏜 것이라 현재 막대만큼 잘리므로 잘린 막대수 += 현재까지 막대수
            cnt += pole
        elif li_1[i] == '(':   # ( 이면 막대 하나가 추가
            pole += 1
        elif li_1[i] == ')':   # ) 이면 막대 하나의 끝이니까 막대수는 하나 감소하고 잘린 막대수 하나 추가
            pole -= 1
            cnt += 1
    print('#{} {}'.format(tc,cnt))
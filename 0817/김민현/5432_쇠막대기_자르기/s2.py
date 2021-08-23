import  sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    iron_bar = input()

    stack = []
    ans = 0

    for i in range(len(iron_bar)):
        #열린 괄호라면
        if iron_bar[i] == '(':
            stack.append('(')
        else:
            # 아닐 경우 빼ㅑ기
            stack.pop()
            if iron_bar[i - 1] == '(':
                #레이저
                ans += cnt
            else:
                ans += 1

    print('#{} {}'.format(tc,ans))

    #스택 사용하지 않고 사용하는법
    for i in range(len(iron_bar)):
        # 열린 괄호라면
        if iron_bar[i] == '(':
            cnt += 1
        else:
            # 아닐 경우 빼ㅑ기
            cnt -= 1
            if iron_bar[i - 1] == '(':
                # 레이저
                ans += cnt
            else:
                ans += 1

    print('#{} {}'.format(tc, ans))
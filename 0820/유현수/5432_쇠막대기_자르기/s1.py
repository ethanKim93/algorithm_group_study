import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = input()
    li = arr.replace('()', 'L')             # ()를 L(laser)로 변경

    result = 0
    bars = 0
    for char in li:
        if char == 'L':             # 레이저를 만나면 쇠막대 개수만큼 result에 추가
            result += bars
        elif char == '(':           # 막대 1개 추가
            bars += 1
        else:                       # 막대 1개를 줄이고 result += 1
            result += 1
            bars -= 1

    print('#{} {}'.format(tc, result))

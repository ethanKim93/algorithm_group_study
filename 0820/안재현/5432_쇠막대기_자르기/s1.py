import sys

sys.stdin = open('sample_input.txt', 'rt', encoding='UTF8')

T = int(input())

for tc in range(0, T):
    N = input()
    steel = 0
    cnt = 0
    i = 0
    while i < len(N):
        if N[i] == '(' and N[i+1] == ')':   # 레이저일 경우
            cnt += steel    # 이전까지 있었던 쇠막대기의 갯수만큼 잘라서 잘린 왼쪽의 막대기들을 cnt에 넣는다.
            i += 2      # () 두개이므로 i에 2 추가
        elif N[i] == '(':   # 쇠막대기 왼쪽 끝일 경우
            steel += 1      # 쇠막대기 갯수 1개 추가
            i += 1
        elif N[i] == ')':   # 쇠막대기 오른쪽 끝일 경우
            cnt += 1       # 오른쪽 쇠막대기 끝은 무조건 잘린 쇠막대기만 있으므로 잘리고 남은 오른쪽의 쇠막대기들을 cnt에 넣는다
            steel -= 1      # 오른쪽 쇠막대기 끝을 지나면 더이상 레이저에 잘리지 않으므로 갯수 제거
            i += 1
    print('#{} {}'.format(tc+1, cnt))   # 잘린 쇠막대기 전체 출력

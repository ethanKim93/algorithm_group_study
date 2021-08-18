import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = []
    ls = []
    # N, M input 받을 변수 선언
    # 열우선 순회를 위한 ls 리스트 선언
    for n in range(N):
        row = input()
        ls.append(row)  #입력받은 문자열을 열우선 순회를 하기 위해 ls 리스트에 저장
        for a in range(N-M+1):
            if row[a:M+a] == row[a:M+a][::-1]:
                answer.append(row[a:M+a])
    # 가로 문자열의 앞 뒤를 바꾸었을 때 서로 일치한다면 answer에 해당 문자열을 추가
    # 문자열의 길이가 앞에서 뒤 끝까지가 아닌 경우 0번 인덱스부터 M번 인덱스까지 반복문을 통해 검사
    for i in range(N):
        col = []
        joincol = ''
        for j in range(N):
            col.append(ls[j][i])
        joincol = ''.join(col)
        if joincol == joincol[::-1]:
            answer.append(joincol)
    for a in range(N-M+1):
        if joincol[a:M+a] == joincol[a:M+a][::-1]:
            answer.append((joincol[a:M+a]))

    answer = ''.join(answer)
    print('#{} {}'.format(tc, answer))
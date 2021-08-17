import sys
sys.stdin = open("sample_input.txt")


def check(target, left, right):
    # 회문 체크를 위한 함수 check 정의
    while left < right:
        # 왼쪽끝과 오른쪽 끝을 비교할 때, 왼쪽 인덱스가 오른쪽 인덱스와 같아질때까지 반복
        if target[left] == target[right]:
            left += 1
            right -= 1
            # 끝이 서로 같으면 왼쪽 인덱스는 1씩 증가, 오른쪽 인덱스는 1씩 감소시켜서 다시 비교
        else:
            return False
    return True


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N = 글자판 배열 행/열 수 , M = 회문 문자열 길이
    li = [input() for _ in range(N)]
    # 글자판 입력받기
    li_rev = [list(li[i][j] for i in range(N)) for j in range(N)]
    # 세로 회문 체크를 위한 리스트 (li[1][0] , li[2][0] , li[3][0] ..)
    result = ''
    for i in range(N):
        for j in range(N-M+1):
            if check(li[i], j, j+M-1):
                # 행 우선순회로 가로 회문 체크하고 True가 나오면 result에 해당 문자열 추가
                result += ''.join(li[i][j:j+M])
            elif check(li_rev[i], j, j+M-1):
                # 가로 회문 체크가 False가 나오면 열 우선 순회로 세로 회문 체크, True면 result에 추가
                result += ''.join(li_rev[i][j:j + M])

    print('#{} {}'.format(tc, result))

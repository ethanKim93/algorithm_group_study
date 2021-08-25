import sys
sys.stdin = open("sample_input.txt")


def card(i, j):
    if i == j:  # group 리스트의 길이가 1이 되면 종료
        return i
    
    first = card(i, (i + j) // 2)   # 더이상 나뉘지 않을 때까지 2개의 그룹으로 나누어 재귀함수를 돌림
    second = card((i + j) // 2 + 1, j)

    if group[first] == 1:  # 앞 그룹이 가위일 때
        if group[second] == 2:
            return second
        elif group[second] == 3:
            return first
        elif group[second] == 1:
            return first
    if group[first] == 2:  # 앞 그룹이 바위일 때
        if group[second] == 1:
            return first
        elif group[second] == 3:
            return second
        elif group[second] == 2:
            return first
    if group[first] == 3:  # 앞 그룹이 보일 때
        if group[second] == 1:
            return second
        elif group[second] == 2:
            return first
        elif group[second] == 3:
            return first


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    group = [0] + list(map(int, input().split()))   # 인덱스가 0일 때 에러를 방지하기 위해 맨 앞에 더해줌.
    print('#{} {}'.format(tc, card(1, N)))
import sys

sys.stdin = open('sample_input.txt')


def findset(x):
    if x == partner[x]:  # 조의 대표번호를 찾을때까지 재귀호출 후 대표번호 return (x를 포함하는 집합을 찾기)
        return x
    else:
        return findset(partner[x])


def union(x, y):
    partner[findset(y)] = findset(x)  # y의 조를 x의 조에 통합 (대표번호 : x의 대표번호)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())    # N : 학생수, M : 파트너 조합 수
    partner = [i for i in range(N + 1)]  # Make-Set, 각각의 번호를 대표번호로 하는 집합 생성
    temp = list(map(int, input().split()))
    for i in range(M):
        x, y = temp[2 * i], temp[2 * i + 1]
        union(x, y)  # 두명 같은조 만들기(y를 x조로)

    for i in range(1, N + 1):
        if partner[i] != i:  # 같은 조원의 번호를 대표 번호로 통일하기
            partner[i] = findset(partner[i])
    answer = len(set(partner[1:]))  # 중복을 제거한 번호의 수가 조의 수(0번제외)
    print('#{} {}'.format(tc, answer))

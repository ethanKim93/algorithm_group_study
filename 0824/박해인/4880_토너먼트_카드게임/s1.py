import sys
sys.stdin = open('sample_input.txt')

# 전체를 두 개의 그룹으로 나누고,
# 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.
def divideandfight(N):
    # base case
    if len(groupa) == 1 and len(groupb) == 1:
        carda = groupa.pop()
        cardb = groupb.pop()
        if carda < cardb: winner = cardb
        if carda > cardb: winner = carda
    groupa = []
    groupb = []

    for i in range(N // 2):
        groupa.append(i)







T = int(input())
for test_case in range(1, T+1):
    N = int(input())  # 인원수 N
    cards = list(map(int, input().split()))
    RSP = {1: '가위', 2: '바위', 3: '보'}
    stack = []

    for c in cards:
        if c == 1: # 가위일때

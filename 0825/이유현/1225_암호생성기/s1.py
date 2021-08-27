import sys
sys.stdin = open('input.txt')


def password(pwd):
    n = 1
    while True:
        p = pwd.pop(0)
        if p > n:
            pwd.append(p-n)
            n += 1
            if n > 5:
                n = 1
        else:
            pwd.append(0)
            return pwd


for tc in range(1, 11):
    tn = int(input())
    pwd = list(map(int, input().split()))

    # 사이클횟수를 줄이기 위한 과정
    minP = pwd[0]
    for p in range(len(pwd)):
        if pwd[p] < minP:
            minP = pwd[p]

    # 8사이클을 돌면 원위치 되므로 1~5의 합인 15로 나눈 몫-1을 15로 곱한 값으로 각각의 번호에서 빼준다
    a = minP // 15
    for p in range(len(pwd)):
        pwd[p] = pwd[p] - (15*(a-1))

    print('#{}'.format(tc), end=' ')
    for p in password(pwd):
        print(p, end=' ')
    print()
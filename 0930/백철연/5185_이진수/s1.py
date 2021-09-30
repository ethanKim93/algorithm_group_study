import sys
sys.stdin = open('sample_input.txt')

T = int(input())
hd = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
# 16진수를 10진수로 변환하기 위한 딕셔너리
for tc in range(1, T+1):
    N, M = map(str, input().split())

    bin = '' # 정답을 저장할 스트링

    for i in M[::-1]: # 16진수를 뒤에서 부터 읽어오는데,
        if i in hd:   # 알파벳으로 되어있는 16진수는
            i = hd[i]  # 딕셔너리와 매칭해서 변환환        n = int(i)
        n = int(i)


        for _ in range(4):    # 십진수를 2진수로 바꿔주기 위한 코드
            bin = str(n % 2) + bin
            n //= 2

    print('#{} {}'.format(tc, bin))


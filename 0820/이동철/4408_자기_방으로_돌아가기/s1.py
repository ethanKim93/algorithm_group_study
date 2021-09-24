import sys
sys.stdin = open('input.txt')

# 이 문제의 핵심은 겹치는 구간이 얼마나 되느냐 이다.
# 따라서 리스트를 하나 만든다음에 학생들의 이동경로마다 카운팅을 해줘서
# 제일 높은 카운팅이 되는곳이 걸리는 시간이 된다.

T = int(input())
for tc in range(1, T + 1):
    check_list = [0] * 201
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        a = (a + 1) // 2
        b = (b + 1) // 2
        for i in range(a, b + 1):
            check_list[i] += 1
    print('#{} {}'.format(tc, max(check_list)))

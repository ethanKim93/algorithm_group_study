# 김주호님의 코드
import sys
sys.stdin = open('sample_input.txt')

for case in range(int(input())):
    pipes = input().split("()")
    total = 0
    num = 0
    for pipe in pipes:
        cnt = 0
        for p in pipe:
            if p == "(":
                num += 1
            elif p == ")":
                num -= 1
                cnt += 1
        total += num + cnt

    print("#{} {}".format(case + 1, total))

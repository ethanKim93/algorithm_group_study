import sys
from math import factorial as f
sys.stdin = open("sample_input.txt")

for case in range(int(input())):
    num = int(input()) // 10

    total = 0
    for i in range(num // 2 + 1):
        j = num - i * 2
        total += 2 ** i * f(i + j) / f(i) / f(j)

    print("#{} {}".format(case + 1, int(total)))
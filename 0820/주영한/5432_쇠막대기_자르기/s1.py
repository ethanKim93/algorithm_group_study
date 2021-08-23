import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    bars = input()
    result = 0
    cnt = 0
    for idx, bar in enumerate(bars):
        if bar == "(":
            cnt += 1
        else:
            cnt -= 1
            if bars[idx - 1] == "(":
                result += cnt
            else:
                result += 1
    print("#{} {}".format(tc, result))
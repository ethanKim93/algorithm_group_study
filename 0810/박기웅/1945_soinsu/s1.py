import sys
sys.stdin = open("input.txt")

primary = [2, 3, 5, 7, 11]

for tc in range(1, int(input())+1):
    nums = []
    N = int(input())
    for p in primary:
        cnt = 0
        while not (N%p):
            N //= p
            cnt += 1
        nums.append(cnt)

    print('#{} {}'.format(tc,' '.join(map(str,nums))))
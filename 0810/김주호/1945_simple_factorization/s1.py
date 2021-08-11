import sys
sys.stdin = open("input.txt")

li = [2, 3, 5, 7, 11]

T = int(input())

for i in range(T):
    print("#{}".format(i + 1), end=" ")
    N = int(input())
    ans = [0] * 5
    for cnt in range(len(li)):
        while True:
            if not N % li[cnt]:
                N /= li[cnt]
                ans[cnt] += 1
            else:
                print("{}".format(ans[cnt]), end=" ")
                break
    print()
import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    prime_factor = [2, 3, 5, 7, 11]
    ans = [0, 0, 0, 0, 0]
    for i in range(5):
        while n%prime_factor[i] == 0:
            ans[i] += 1
            n = n//prime_factor[i]


    print("#{} {}".format(tc, " ".join(map(str,ans))))
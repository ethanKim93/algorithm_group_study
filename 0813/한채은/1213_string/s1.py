import sys
sys.stdin = open("test_input.txt", encoding="UTF-8")

for tc in range(10):
    T = int(input())
    target = input()
    S = input()
    cnt = 0
    for i in range(len(S)):
        if S[i] == target[0]:
            if S[i:i+len(target)] == target:
                cnt += 1
    print("#{} {}".format(T, cnt))


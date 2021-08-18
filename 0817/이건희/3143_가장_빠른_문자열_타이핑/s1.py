import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t + 1):
    text, word = input().split()
    temps = cnt = 0
    for i in range(len(text)):
        i += temps
        if i >= len(text):
            break

        elif text[i:i + len(word)] == word:
            temps += len(word) - 1

        cnt += 1

    print("#{} {}".format(tc, cnt))

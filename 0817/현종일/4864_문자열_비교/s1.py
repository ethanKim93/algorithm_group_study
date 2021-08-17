import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    target = input()
    sent = input()
    idx = 0
    result = 0
    while True:
        cnt = 0
        if idx > len(sent) - len(target):
            break

        for i in range(len(target)):
            if sent[idx + i] == target[i]:
                cnt += 1
            else:
                break

        if not cnt:
            idx += 1
        else:
            idx += cnt

        if cnt == len(target):
            result += 1

    print('#{} {}'.format(tc, result))

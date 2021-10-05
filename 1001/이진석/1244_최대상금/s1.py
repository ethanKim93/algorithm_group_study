import sys
sys.stdin = open("input.txt")

def complete_change(cnt):
    same_idx = 0
    for i in range(len(prize)):
        for j in range(i + 1, len(prize)):
            if prize[i] == prize[j]:
                same_idx = (i, j)

    while cnt:
        if same_idx:
            prize[same_idx[0]], prize[same_idx[1]] = prize[same_idx[1]], prize[same_idx[0]]
        else:
            prize[-1], prize[-2] = prize[-2], prize[-1]
        cnt -= 1

for tc in range(1, int(input())+1):
    prize, exc = input().split()
    prize = list(prize)             # mutable
    exc = int(exc)                  # 교환횟수
    visited = [0] * len(prize)      #
    for i in range(len(prize)-1):
        if prize[i] == max(prize[i:]):
            visited[i] = 1

    i = -1
    while i < len(prize) and exc and 0 in visited:
        i += 1
        if visited[i]:
            continue
        else:
            max_prize = prize[i]
            max_idx = i
            for j in range(i+1, len(prize)):
                if prize[j] >= max_prize:       # 중복됐을때 가장 뒤에꺼
                    max_prize = prize[j]
                    max_idx = j
            prize[i], prize[max_idx] = prize[max_idx], prize[i]
            for k in range(len(prize)):
                if prize[k] == max(prize[k:]):
                    visited[k] = 1
        exc -= 1

    if exc:
        complete_change(exc)



    answer = ''.join(prize)
    print('#{} {}'.format(tc, answer))
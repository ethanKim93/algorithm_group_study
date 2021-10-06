import sys
sys.stdin = open('sample_input.txt')

def is_run(lst):
    count = [0] * 10
    for i in lst:
        count[i] += 1
    for j in range(0, 10-2):
        if count[j] >= 1 and count[j+1] >= 1 and count[j+2] >= 1:
            return True
    return False

def is_triplet(lst):
    count = [0] * 10
    for i in lst:
        count[i] += 1
    for j in range(10):
        if count[j] >= 3:
            return True
    return False


def is_babygin(lst):
    if is_run(lst) or is_triplet(lst):
        return True
    else:
        return False

T = int(input())
for test_case in range(1, T+1):
    data = list(map(int, input().split()))

    winner = 0
    p1 = []
    p2 = []
    for i in range(len(data)):
        if i % 2 == 0:
            p1.append(data[i])
            if len(p1) >= 3:  # 3장이상일 때부터 babygin check
                if is_babygin(p1):
                    winner = 1
                    break
        else:
            p2.append(data[i])
            if len(p2) >= 3:  # 3장이상일 때부터 babygin check
                if is_babygin(p2):
                    winner = 2
                    break

    print('#{} {}'.format(test_case, winner))
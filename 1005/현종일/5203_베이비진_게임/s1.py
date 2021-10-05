import sys
sys.stdin = open("sample_input.txt")

def check(p):
    for j in range(10):
        if p[j] == 3:
            return True
        if j < 8:
            if p[j] and p[j + 1] and p[j + 2]:
                return True
    return False



for tc in range(1, int(input())+1):
    cards = (list(map(int, input().split())))

    p1 = [0] * 10
    p2 = [0] * 10
    winner = 0

    for i in range(len(cards)//2):
        p1[cards[i*2]] += 1
        p2[cards[i * 2 + 1]] += 1

        if check(p1):
            winner = 1
            break

        elif check(p2):
            winner = 2
            break

    print("#{} {}".format(tc, winner))






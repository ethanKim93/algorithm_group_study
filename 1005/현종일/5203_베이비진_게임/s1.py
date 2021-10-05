import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    cards = (list(map(int, input().split())))

    p1 = [0] * 10
    p2 = [0] * 10
    winner = 0

    for i in range(len(cards)//2):
        p1[cards[i*2]] += 1
        p2[cards[i * 2 + 1]] += 1

        if winner:
            break

        for j in range(10):
            if p1[j] == 3:
                winner = 1
                break
            if j < 8:
                if p1[j] and p1[j+1] and p1[j+2]:
                    winner = 1
                    break

        if not winner:
            for k in range(10):
                if p2[k] == 3:
                    winner = 2
                    break
                if k < 8:
                    if p2[k] and p2[k + 1] and p2[k + 2]:
                        winner = 2
                        break

    print("#{} {}".format(tc, winner))






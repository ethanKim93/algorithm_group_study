def itoa(kanji):
    total = 0
    for i in range(len(kanji)):
        total *= 10
        total += ord(kanji[i]) - 48
    return total

n = itoa(input())
print(n)


TC = int(input())

for tc in range(1, TC+1):
    patt = input()
    sentence = input()

    result = 0
    for i in range(len(sentence)-len(patt)+1):
        if sentence[i:i+len(patt)] == patt:
            result = 1


    print('#{} {}'.format(tc, result))
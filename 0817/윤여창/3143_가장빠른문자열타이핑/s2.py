import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    sentence, patt = input().split()
    cunt = 0
    i = 0
    while i <= len(sentence):
        if sentence[i:i+len(patt)] == patt:
            cunt += 1
            i += len(patt)
        else:
            i += 1
    result = len(sentence)-cunt*(len(patt)-1)
    print('#{} {}' .format(t, result))

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    patt = input()
    sentence = input()
    dicct = {}
    for i in patt:
        dicct[i] = 0
    for j in sentence:
        if j in dicct:
            dicct[j] += 1
    print("#{} {}".format(tc, max(dicct.values())))

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    patt = input()
    sentence = input()

    li = []
    for i in patt:
        li.append(sentence.count(i))

    print("#{} {}".format(tc, max(li)))
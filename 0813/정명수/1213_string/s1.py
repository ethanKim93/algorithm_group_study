import sys
sys.stdin = open('input.txt')

for test_case in range(10):
    T = int(input())
    target = input()
    sentence = input()
    M = len(sentence)
    N = len(target)
    i = 0
    count = 0
    while i != (M-N+1):
        j = 0
        while target[j] == sentence[i+j]:
            j += 1
            if j == N:
                count += 1
                break

        i += 1
    print('#{} {}'.format(T,count))
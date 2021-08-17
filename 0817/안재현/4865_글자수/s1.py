import sys

sys.stdin = open('sample_input.txt', 'rt', encoding='UTF8')

T = int(input())
dic = {}
result = 0
for i in range(0, T):
    N = input()
    M = input()

    for j in N:
        dic[j] = 0

    for key, values in dic.items():
        for a in range(0, len(M)):
            if key == M[a]:
                dic[key] += 1
                for val in dic.values():
                    if dic[key] > result:
                        result = dic[key]
    print('#{} {}'.format(i+1, result))
    dic = {}
    result = 0
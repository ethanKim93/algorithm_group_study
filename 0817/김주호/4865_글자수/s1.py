import sys
sys.stdin = open("sample_input.txt")

for case in range(int(input())):
    N = set(input())
    M = input()

    dic = {}
    for i in range(len(M)):
        try:
            dic[M[i]] += 1
        except:
            dic[M[i]] = 1

    total = 0
    for j in N:
        if dic[j] > total:
            total = dic[j]

    print("#{} {}".format(case + 1, total))
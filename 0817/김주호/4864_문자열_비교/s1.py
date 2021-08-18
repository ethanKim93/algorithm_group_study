import sys
sys.stdin = open("sample_input.txt")

for case in range(int(input())):
    N = input()
    M = input()

    answer = 0
    for i in range(len(M) - len(N) + 1):
        for j in range(len(N)):
            if M[i + j] != N[j]:
                break
        else:
            answer = 1
            break

    print("#{} {}".format(case + 1, answer))
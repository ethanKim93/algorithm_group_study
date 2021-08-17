import sys
sys.stdin = open("sample_input.txt")

for case in range(int(input())):
    A, B = input().split()

    cnt = 0
    i = 0
    while i < len(A) - len(B) + 1:
        for j in range(len(B)):
            if A[i + j] != B[j]:
                i += 1 if j == 0 else j
                break
        else:
            cnt += 1
            i += len(B)

    print("#{} {}".format(case + 1, len(A) - cnt * (len(B) - 1)))
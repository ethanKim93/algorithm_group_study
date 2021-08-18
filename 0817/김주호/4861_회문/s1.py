import sys
sys.stdin = open("sample_input.txt")

for case in range(int(input())):
    N, M = map(int, input().split())

    li = [input() for _ in range(N)]

    ans = ""
    for i in range(N):
        st = [0, 0]
        for j in range(N - M + 1):
            st[0] = li[i][j: j + M]
            st[1] = ''.join([k[i] for k in li[j: j + M]])

            for l in range(2):
                if st[l] == st[l][::-1]:
                    ans = st[l]
                    break

            if len(ans):
                break
        if len(ans):
            break

    print("#{} {}".format(case+1, ans))
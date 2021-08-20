import sys
sys.stdin = open("input.txt")

def word(M):
    i = 0
    while i < len(M)-1:
        if M[i] == M[i+1]:
            M.pop(i)
            M.pop(i)
            word(M)
        else:
            i+=1
    return M

for tc in range(1,11):
    N, M = map(str,input().split())
    M = list(M)
    print('#{} {}'.format(tc, "".join(word(M))))
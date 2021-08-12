import sys
sys.stdin = open("sample_input.txt")


class Search:
    def __init__(self, e, P):
        self.s = 1
        self.e = e
        self.P = P
        self.c = 0
        self.cnt = 1

    def binary(self):
        while self.P != self.c:
            self.c = int((self.s + self.e) / 2)
            if self.P < self.c:
                self.e = self.c
                self.cnt += 1
            if self.P > self.c:
                self.s = self.c
                self.cnt += 1
        return self.cnt


T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int,input().split())

    a = Search(P, Pa)
    result_a = a.binary()
    b = Search(P, Pb)
    result_b = b.binary()

    if result_a < result_b:
        result = 'A'
    elif result_a > result_b :
        result = 'B'
    else:
        result = 0
    print('#{} {}'.format(tc, result))




import sys
sys.stdin = open("input.txt")

def permutation(k):
    if k == n_length:
        temps2 = int(''.join(map(str,temps)))
        permutated_int.append(temps2)
        return

    for i in range(n_length):
        if temps[i] == -1:
            temps[i] = n[k]
            permutation(k+1)
            temps[i] = -1

def checking():
    while permutated:
        test = permutated.pop(0)
        # 비교하자마자 같다면
        if n == test:
            if pos % 2 == 0:
                return test

        # 비교시작
        check_cnt = 0
        for i in range(n_length):
            if n[i] != test[i]:
                check_cnt += 1

        if check_cnt <= pos*2:
            return test

        # 교환횟수 못잡음 -> Fail


for tc in range(1,int(input())+1):
    n, pos = input().split()
    n, pos = list(n), int(pos)

    n_length = len(n)
    temps = [-1] * n_length
    permutated_int = []
    permutation(0)

    permutated_int = sorted(permutated_int,reverse=True)

    permutated = list(map(lambda x: str(x), permutated_int))

    # print(*permutated,sep="\n")

    print("#{} {}".format(tc, checking()))

# Fail: Wrong answer
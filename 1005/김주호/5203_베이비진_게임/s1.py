def check(human):
    cnt = 0
    for c in human:
        if c > 0:
            cnt += 1
        else:
            cnt = 0

        if c >= 3 or cnt >= 3:
            return True

    return False


for case in range(int(input())):
    A = [0] * 10
    B = [0] * 10

    pick = list(map(int, input().split()))
    print("#{}".format(case + 1), end=" ")

    for i in range(0, 12, 2):
        A[pick[i]] += 1
        B[pick[i+1]] += 1

        if i >= 2:
            if check(A):
                print(1)
                break
            if check(B):
                print(2)
                break
    else:
        print(0)

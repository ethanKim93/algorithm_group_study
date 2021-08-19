def fibo(n):
    global cnt
    cnt += 1
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


cnt = 0
print(fibo(15), cnt)



def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.appen(fibo1(n-1) + fibo(n-2))
    return memo[n]


memo = [0, 1]

print(fibo(15))


def fibo2(n):
    global cnt
    cnt += 1
    if n >= 2 and memo2[n] == 0:
        memo2[n] = fibo2(n-1) + fibo2(n-2)
    return memo2[n]


def fibo3(n):
    if n >= 2 and len(memo3) <= n:
        memo3.append(fibo3(n-1) + fibo3(n-2))
    return memo3[n]


n = 10
memo2 = [0] * (n + 1)
memo2[0] = 0
memo2[1] = 1
cnt = 0
print(fibo2(n), cnt)

memo3 = [0, 1]
print(fibo3(n))




#6
def divisor(n):
    divisors = []
    divisors_back = []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != (n // i):
                divisors_back.append(n // i)

    return (divisors + divisors_back[::-1])[1]


arr = [(i, divisor(i)) for i in range(2, 1000001)]
arr.sort(key=lambda x: (-x[1], -x[0]))

print(arr[230000], arr[230001], arr[230002])
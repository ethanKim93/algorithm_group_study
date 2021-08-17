x = input()


def reverse_slice(n):
    lst = [0] * len(n)
    cnt = 1
    ans = ''
    for i in n:
        lst[len(lst) - cnt] = i
        cnt += 1
    for j in lst:
        ans += j
    return ans


reverse_word = reverse_slice(x)
print(reverse_word)

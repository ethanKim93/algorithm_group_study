def itoa(idx): # int >> str
    ans = ""
    temps = []

    if idx < 0:
        idx = -idx
        ans += "-"

    while idx > 0:
        temps.insert(0, chr(48 + idx%10))
        idx //= 10

    if not idx:
        ans += chr(48)

    for i in temps:
        ans += i

    return ans

def aoti(idx): # str >> int
    ans = 0
    for i in range(len(idx)):
        ans += (ord(idx[i])-48) * 10**(len(idx)-1-i)

    return ans



print(itoa(2020))
print(itoa(-2020))
print(itoa(20))
print(itoa(0))
print(aoti("2021"))
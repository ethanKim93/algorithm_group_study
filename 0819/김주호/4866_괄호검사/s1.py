import sys
sys.stdin = open("sample_input.txt")

dic = {")": "(", "}": "{"}

for case in range(int(input())):
    st = input()
    li = []
    val = 1
    for ch in st:
        if ch == "(" or ch == "{":
            li.append(ch)
        elif ch == ")" or ch == "}":
            if len(li) != 0 and dic[ch] == li[-1]:
                li.pop()
            else:
                val = 0
                break
    print("#{} {}".format(case + 1, val if len(li) == 0 else 0))

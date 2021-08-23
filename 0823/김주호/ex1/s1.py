def func(st):
    stack = []

    for ch in st:
        if "0" <= ch <= "9":
            print(ch, end=" ")
        elif ch == " ":
            pass
        else:
            stack.append(ch)

    while stack:
        print(stack.pop(), end=" ")


func("2 + 3 * 4 / 5")
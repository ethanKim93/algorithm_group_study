for case in range(int(input())):
    li = [[0] for _ in range(5)]

    high = 0
    for i in range(5):
        li[i] = input()
        if high < len(li[i]):
            high = len(li[i])

    st = []

    for col in range(high):
        for row in range(5):
            try:
                st.append(li[row][col])
            except:
                pass

    print("#{} {}".format(case + 1, ''.join(st)))
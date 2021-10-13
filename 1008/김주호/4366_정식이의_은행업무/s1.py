for case in range(int(input())):
    two = list(map(int, (input())))
    three = list(map(int, (input())))

    nums = []
    for i in range(len(two)):
        two[i] ^= 1
        num = 0
        for j in range(len(two)):
            num += two[len(two) - 1 - j] << j
        nums.append(num)
        two[i] ^= 1

    flag = False
    for i in range(len(three)):
        for _ in range(2):
            three[i] += 1
            three[i] %= 3
            num = 0
            for j in range(len(three)):
                num += three[len(three) - 1 - j] * (3 ** j)
            if num in nums:
                print("#{} {}".format(case + 1, num))
                flag = True
                break

        three[i] += 1
        three[i] %= 3

        if flag:
            break

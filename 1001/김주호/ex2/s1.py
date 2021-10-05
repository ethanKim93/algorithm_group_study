def babygin(idx=0):
    if idx == 6:
        collections.add(''.join(arr))
        return
    for i in range(6):
        if check[i]:
            arr[idx] = nums[i]
            check[i] = False
            babygin(idx+1)
            check[i] = True


st = ["124783", "667767", "054060", "101123"]

for nums in st:

    check = [True] * 6
    arr = [""] * 6

    collections = set()

    babygin()

    while collections:
        collection = list(map(int, collections.pop()))
        run = triple = False

        for i in range(0, 6, 3):
            if collection[i] == collection[i+1] == collection[i+2]:
                run = True
            elif collection[i] + 2 == collection[i+1] + 1 == collection[i+2]:
                triple = True

        if run and triple:
            print("{} can be babygin".format(nums))
            break


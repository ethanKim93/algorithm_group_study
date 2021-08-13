def itoa(nums):
    st = ''
    if nums < 0 :
        nums *= -1
        st += "-"

    llist = []
    while nums > 0 :
        num = nums % 10 # 맨 뒤에서부터
        llist.insert(0, chr(num + 48)) # 추출하고 리스트에 담아주기
        nums = int(nums//10)

    for i in range(len(llist)):
        st += llist[i]

    return st
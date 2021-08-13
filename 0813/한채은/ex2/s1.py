def itoa(nums,s):
    llist = []
    while n > 0 :
        num = nums % 10 # 맨 뒤에서부터
        llist.insert(0, chr(num + 48)) # 추출하고 리스트에 담아주기
        nums = int(nums//10)
    s = "".join(llist)
    print(s)
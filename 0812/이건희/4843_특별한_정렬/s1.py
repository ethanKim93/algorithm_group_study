import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    num = int(input())
    num_list = list(map(int,input().split()))
    #select sort
    for i in range(num):
        if i%2 == 0: # idx : 0, 2, 4, 6...
            mx = 0
            for x in range(i, num): # =max(num_list[i:])
                if mx < num_list[x]:
                    mx_idx, mx = x, num_list[x]
            num_list[i], num_list[mx_idx] = num_list[mx_idx], num_list[i]

        else: # idx : 1, 3 ,5 7...
            mn = 100
            for x in range(i, num): # =min(num_list[i:])
                if mn > num_list[x]:
                    mn_idx, mn = x, num_list[x]
            num_list[i], num_list[mn_idx] = num_list[mn_idx], num_list[i]

    # Print
    print("#{} {}".format(tc, " ".join(map(str,num_list[:10]))))
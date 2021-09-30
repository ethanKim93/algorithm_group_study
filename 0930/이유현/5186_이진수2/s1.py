import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    dec = float(input())
    dec_bin = []
    S = ['9', '9']

    while(S[1] != '0' and len(dec_bin) <= 12):
        dec *= 2
        S = str(dec).split('.')
        dec_bin.append(S[0])
        dec = float('0.' + S[1])
    if len(dec_bin) > 12:
        print('#{} overflow'.format(tc))

    else:
        print("#{}".format(tc),''.join(dec_bin))
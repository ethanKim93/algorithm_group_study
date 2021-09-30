# hex_str = '0DEC'
hex_str = '0269FAC9A0'
pwd_pattern = {
    '001101': '0',
    '010011': '1',
    '111011': '2',
    '110001': '3',
    '100011': '4',
    '110111': '5',
    '001011': '6',
    '111101': '7',
    '011001': '8',
    '101111': '9',
}

hex_dec = []
for hex in hex_str:
    hex_dec.append(int(hex, 16))

bin_str = ''
for bin in hex_dec:
    bin_str += '{0:b}'.format(bin).zfill(4)

i = 0
while i < len(bin_str)-6:
    if bin_str[i:i+6] in list(pwd_pattern.keys()):
        print(pwd_pattern[bin_str[i:i+6]], end=' ')
        i += 6
    else:
        i += 1
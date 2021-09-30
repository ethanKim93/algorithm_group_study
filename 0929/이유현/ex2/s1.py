# hex_str = '0F97A3'
hex_str = '01D06079861D79F99F'

hex_dec = []
for hex in hex_str:
    hex_dec.append(int(hex, 16))

bin_str = ''
for bin in hex_dec:
    bin_str += '{0:b}'.format(bin).zfill(4)

for i in range(0, len(bin_str), 7):
    print(int(bin_str[i:i+7], 2), end=' ')
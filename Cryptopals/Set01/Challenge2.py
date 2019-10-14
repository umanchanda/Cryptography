import binascii

def fixed_xor(s, t):
    bin_s = [ord(chr(c)) for c in binascii.unhexlify(s)]

    xor = [a^b for a,b in zip(bin_s, binascii.unhexlify(t))]

    xor_str = "".join([hex(a) for a in xor])
    hex_str = "".join([a for a in xor_str.split('0x')])
    return(hex_str)

def main():
    s = "1c0111001f010100061a024b53535009181c"
    t = "686974207468652062756c6c277320657965"
    print(fixed_xor(s, t))

if __name__ == "__main__":
    main()
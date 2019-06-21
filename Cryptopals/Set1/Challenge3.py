import binascii

def xor_cipher(s):
    strs = []
    bin_s = [ord(chr(c)) for c in binascii.unhexlify(s)]

    for char in range(256):
        xor = [a^b for a,b in zip(bin_s, [char] * len(bin_s))]
        xor_str = chr(char) + ": " + "".join([chr(a) for a in xor])
        strs.append(xor_str)
    return(strs)

def main():
    s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    for i in xor_cipher(s):
        print(i)

if __name__ == "__main__":
    main()
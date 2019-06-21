import binascii

def repeating_key_xor(s, key):
    keylen = len(key)
    i = 0
    cipher = []
    for c in s:
        xor = ord(c) ^ ord(key[i % keylen])
        cipher.append(hex(xor))
        i += 1
    ciphertext_hex = "".join(cipher)
    ciphertext = "".join([a for a in ciphertext_hex.split('0x')])
    return ciphertext

def main():
    s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    print(repeating_key_xor(s, "ICE"))


if __name__ == "__main__":
    main()
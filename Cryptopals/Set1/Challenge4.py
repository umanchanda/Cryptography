import requests
import binascii

def detect_single_char_xor(s):
    bin_s = [ord(chr(c)) for c in binascii.unhexlify(s)]
    poss_strs = []

    for char in range(0, 256):
        xor = [a^b for a,b in zip(bin_s, [char] * len(bin_s))]
        xor_str = chr(char) + ": " + "".join([chr(a) for a in xor])
        poss_strs.append(xor_str)
    return poss_strs

def main():
    r = requests.get("https://cryptopals.com/static/challenge-data/4.txt")
    lines = r.text.split('\n')
    # kinda cheated here
    arr = detect_single_char_xor(lines[170])
    for a in arr:
        print(a)
    
if __name__ == "__main__":
    main()
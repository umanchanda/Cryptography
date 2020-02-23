import binascii
import requests
import random

def hamming_distance(s, t):

    s_binary = [c for c in s.encode()]
    t_binary = [d for d in t.encode()]
    xor = [a^b for a,b in zip(s_binary, t_binary)]

    if len(s_binary) != len(t_binary):
        return -1

    hamming = 0
    for byte in xor:
        for bit in bin(byte):
            if bit == '1':
                hamming += 1
    return hamming

def normalized_edit_distance(cipher, keysize):
    c = [cipher[i:i+keysize] for i in range(0, len(cipher), keysize)]
    return c

def main():
    r = requests.get('http://cryptopals.com/static/challenge-data/6.txt')
    lines = r.text.split('\n')
    k = min(random.randint(2, 41), random.randint(2, 41))
    for line in lines:
        print(normalized_edit_distance(line, k))

if __name__ == "__main__":
    main()
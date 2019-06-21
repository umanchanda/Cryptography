import requests
import base64
from Crypto.Cipher import AES

def implementcbc():
    pass

def decryptcbc(cipher, key):
    cipher = base64.b64decode(cipher)
    iv = cipher[:16]
    decipher = AES.new(key, AES.MODE_CBC, iv)
    return decipher.decrypt(cipher[16:]).decode('utf-8')

def main():
    r = requests.get('http://cryptopals.com/static/challenge-data/10.txt')
    text = r.text
    key = 'YELLOW SUBMARINE'
    print(decryptcbc(text, key))


if __name__ == "__main__":
    main()
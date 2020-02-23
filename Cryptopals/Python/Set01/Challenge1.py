import binascii

def hex_to_base64(hex_str):
    base64_str = binascii.b2a_base64(binascii.unhexlify(hex_str))
    base64 = base64_str.decode('utf-8')
    return(base64)

def main():
    hex_str="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(hex_to_base64(hex_str))

if __name__ == "__main__":
    main()
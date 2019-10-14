
def pkcs7padding(text, length):
    if length > len(text):
        difference = length - len(text)
        text = text + difference * '\x04'
    return text
    

def main():
    print(pkcs7padding('YELLOW SUBMARINE', 20))

if __name__ == "__main__":
    main()
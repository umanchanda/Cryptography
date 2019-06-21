import requests

def countrepetitions(cipher):
    chunks = [cipher[i:i+16] for i in range(0, len(cipher), 16)]
    return len(chunks) - len(set(chunks))

def main():
    r = requests.get('http://cryptopals.com/static/challenge-data/8.txt')
    lines = r.text.split('\n')
    numrepetitions = []
    for line in lines[:-1]:
        numrepetitions.append(countrepetitions(line))
    maxrepetitions = max(numrepetitions)
    index = numrepetitions.index(maxrepetitions)
    print("{} at line {}".format(lines[index], index+1))


if __name__ == "__main__":
    main()
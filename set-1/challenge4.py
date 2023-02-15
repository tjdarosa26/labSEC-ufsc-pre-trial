
import urllib3
import challenge3 


url = 'https://cryptopals.com/static/challenge-data/4.txt'
http = urllib3.PoolManager()
response = http.request('GET', url)


hexString = str(response.data)[2:-1]
hexStringsArr = hexString.split('\\n')


def findSingleCharEncrypted(hexStringsArr:list[str]) -> str:
    
    bestPunctuation = 0
    index = 0
    key = 0

    for i in range(len(hexStringsArr)):

        key, points = challenge3.singleByteXOR(hexStringsArr[i])

        if points > bestPunctuation:
            bestPunctuation = points
            key = key
            index = i

    return hexStringsArr[index], index, key


def main():
    result, index, key = findSingleCharEncrypted(hexStringsArr)
    meaning = challenge3.main(result).replace("\n", '')

    print(f"""
The string encrypted by single-character XOR is:
{result}
Which is the {index + 1}th of those reveived as input.
And means: '{meaning}'.
The key to decrypt the message is: {key}.
    """)
    

if __name__ == '__main__':
    main()







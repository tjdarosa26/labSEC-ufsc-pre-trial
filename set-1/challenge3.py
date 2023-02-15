
import codecs


hexString = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'


def singleByteXOR(hexString:str) -> int:
    hexBytes = codecs.decode(hexString, 'hex')

    bestPunctuation = 0
    key = 0
    for i in range(256):
        xoredHexBytes = XORer(hexBytes, i)
        xoredString = codecs.decode(xoredHexBytes, 'latin-1')

        # I searched about "ETAOIN SHRDLU" and discovered that those are
        # the most frequent chars of the English language. I also took the tip
        # from the challenge that says 'Character frequency is a good 
        # metric.' So, i ended up using char frequency to give each string
        # a punctuation about their English likeliness and took the string with
        # the best score to be decoded.
        punctuation = englishLikePoints(xoredString)
       
        if punctuation > bestPunctuation:
            bestPunctuation = punctuation
            key = i

    return key, bestPunctuation


def XORer(stringBytes:bytes, x:int) -> bytearray:
    result = bytearray()
    for i in stringBytes:
        xoredByte = i ^ x
        result.append(xoredByte)

    return result


def englishLikePoints(string:str) -> int:
    mostCommonChars = 'etaoin shrdlu'
    points = 0
    for i in string:
        if mostCommonChars.find(i) != -1:
            points += 1

    return points


# Decrypting the message

# The function accepts args because it is also used in the 4th challenge,
# and one arg is sent from there.

def main(*args):
    hexStringFromArgs = None
    if len(args) > 0:
        hexStringFromArgs = args[0]

    if hexStringFromArgs:
        key, bestPunctuation = singleByteXOR(hexStringFromArgs)
        hexBytes = codecs.decode(hexStringFromArgs, 'hex')  
    else:
        key, bestPunctuation = singleByteXOR(hexString)
        hexBytes = codecs.decode(hexString, 'hex')

    xoredHexBytes = XORer(hexBytes, key)
    message = codecs.decode(xoredHexBytes, 'utf-8')

    if not(hexStringFromArgs):
        print(f"""
{message}
The best punctuation was >> {bestPunctuation} <<
        """)

    return message

if __name__ == '__main__':
    main()
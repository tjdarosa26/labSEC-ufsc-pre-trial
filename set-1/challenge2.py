
import codecs

buffer1 = '1c0111001f010100061a024b53535009181c'
buffer2 = '686974207468652062756c6c277320657965'

def fixedXOR(buffer1, buffer2):

    result = bytearray()

    buffer1Bin = codecs.decode(buffer1, 'hex')
    buffer2Bin = codecs.decode(buffer2, 'hex')

    for i in range(len(buffer1Bin)):
        result.append(buffer1Bin[i] ^ buffer2Bin[i])

    return str(codecs.encode(result, 'hex'))[2:-1]

def main():
    result = fixedXOR(buffer1, buffer2)
    print(result)

if __name__ == '__main__':
    main()

        


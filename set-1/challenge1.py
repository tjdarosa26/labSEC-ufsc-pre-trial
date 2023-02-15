
import codecs

hexString = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

def hexToBase64String(hexString:str):

    hex = codecs.decode(hexString, 'hex')
    base64 = codecs.encode(hex, 'base64')
    base64String = base64.decode('utf-8')
 
    return base64String

def main():
    result = hexToBase64String(hexString)
    print(result.replace('\n', ''))

if __name__ == '__main__':
    main()








import json
import sys
# from random import randrange # for randomly-generated codes


def encrypt(text, codes):
    """
    Encrypts a string based on a conversion dictionary.

    Arguments:
        text: the text to be encrypted
        codes: the encryption dictionary
    """
    for vowel, code in codes.items():
        text = text.replace(vowel, code)
    return text


def decrypt(text, codes):
    """
    Decrypts a string based on a conversion dictionary.

    Arguments:
        text: the text to be decrypted
        codes: the encryption dictionary
    """
    reverse_codes = dict((v, k) for k, v in codes.items())
    for code, vowel in reverse_codes.items():
        text = text.replace(code, vowel)
    print(text)
    return text


def main(text, mode, codes):
    if mode == 'encrypt':
        result = encrypt(text, codes)
    if mode == 'decrypt':
        result = decrypt(text, codes)
    print(f'Your {mode}ed text is: {result}')


if __name__ == "__main__":
    text = sys.argv[1]
    mode = sys.argv[2].lower()
    if len(sys.argv) == 3:  # Codes not provided, so use default
        codes = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
    else:  # Codes passed as command line argument
        codes = json.loads(sys.argv[3])
    # Optionally, codes could be hard-coded and not passed as a command-line argument
    # Or codes could be randomly generated using the snippet here:
    # conversion_dict = {vowel: str(randrange(10))
    #                    for vowel in ['a', 'e', 'i', 'o', 'u']}
    if mode not in ['decrypt', 'encrypt']:
        raise Exception(
            "Second argument should be a mode: \'decrypt\' or \'encrypt\'")
    main(text, mode, codes)

# Encryption/Decryption

Testing library: `pip install pytest`

To run (example): `python main.py 'another message here!' encrypt '{"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}'` (encryption) or `python main.py 'th3s 3s 1 m2ss1g2.' decrypt '{"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}'` (decryption). The first argument is the text, the second is the mode (encryption or decryption) and the third is the code.

To test: `pytest`

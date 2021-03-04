import main


def test_decrypt():
    text = 'th3s 3s 1 m2ss1g2.'
    codes = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
    assert main.decrypt(text, codes) == "this is a message."


def test_encrypt():
    text = "another message here!"
    codes = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
    assert main.encrypt(text, codes) == "1n4th2r m2ss1g2 h2r2!"

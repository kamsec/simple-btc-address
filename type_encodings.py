# implementation of the encodings

from hashlib import sha256

base58_alphabet = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

# x = 'FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141'
def hex_to_int(x):
    x = int(x.replace(' ', ''), 16)
    return x

def int_to_hex_zfill(x):
    x = hex(x)[2:].zfill(64).upper()
    return x

def b58encode_int(x, default_one=True):
    if not x and default_one:
        return base58_alphabet[0:1]
    base = len(base58_alphabet)
    string = b''
    while x:
        x, remainder = divmod(x, base)
        string = base58_alphabet[remainder:remainder+1] + string
    return string

def b58encode(x):
    old_len = len(x)
    x = x.lstrip(b'\0')
    new_len = len(x)
    acc = int.from_bytes(x, byteorder='big')  # first byte is the most significant
    result = b58encode_int(acc, default_one=False)
    return base58_alphabet[0:1] * (old_len - new_len) + result

def b58encode_check(x):
    digest = sha256(sha256(x).digest()).digest()
    return b58encode(x + digest[:4])

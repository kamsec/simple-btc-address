# implementation of the address conversions

import base64
import hashlib
from hashlib import sha256
from type_encodings import b58encode, b58encode_check, int_to_hex_zfill

def convert_private_key(private_key_int):
    print(f'Private key (int): {private_key_int}')

    # to hex
    private_key_hex = int_to_hex_zfill(private_key_int)
    print(f'Private key (hex): {private_key_hex}')

    # to base64
    private_key_hex_bytes = bytes.fromhex(private_key_hex)
    private_key_base64 = base64.b64encode(private_key_hex_bytes).decode("utf-8")
    print(f'Private key (base64): {private_key_base64}')

    # to WIF
    private_key_hex_px = '80' + private_key_hex  # prefix 0x80 for mainnet, 0xef for testnet
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    private_key_WIF = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")  # decode removes b''
    print(f'Private key (WIF): {private_key_WIF}')

    # to WIF compressed
    private_key_hex_compressed_px = '80' + private_key_hex + '01'  # suffix 01 - compresed public key, none otherwise
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksum
    private_key_WIF_compressed = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    print(f'Private key (WIF compressed): {private_key_WIF_compressed}')


def compress_public_key(public_key_with_prefix_uncompressed):
    if int(public_key_with_prefix_uncompressed, 16) & 1 == 1:  # odd
        public_key_compressed = '03' + public_key_with_prefix_uncompressed[2:66]  # replaces 04 and removes Y-coordinate
    else:  # even
        public_key_compressed = '02' + public_key_with_prefix_uncompressed[2:66]  # replaces 04 and removes Y-coordinate
    return public_key_compressed

# requires format '04' + Point.x + Point.y
def convert_public_key(public_point):
    print(f'Public point: {public_point}')

    # to public key uncompressed
    public_key_uncompressed = '04' + int_to_hex_zfill(public_point.x) + int_to_hex_zfill(public_point.y)
    print(f'Public key (uncompressed): {public_key_uncompressed}')

    # to Bitcoin address uncompressed
    address = public_key_uncompressed
    address_sha256 = sha256(bytes.fromhex(address)).hexdigest()
    address_sha256_ripemd160 = hashlib.new('ripemd160', bytes.fromhex(address_sha256)).hexdigest()
    address_sha256_ripemd160_00 = '00' + address_sha256_ripemd160
    address_sha256_ripemd160_00_base58check = b58encode_check(bytes.fromhex(address_sha256_ripemd160_00)).decode("utf-8")
    print(f'Bitcoin address (uncompressed): {address_sha256_ripemd160_00_base58check}')

    # to public key compressed
    public_key_compressed = compress_public_key(public_key_uncompressed)
    print(f'Public key (compressed): {public_key_compressed}')

    # to Bitcoin address compressed
    address = public_key_compressed
    address_sha256 = sha256(bytes.fromhex(address)).hexdigest()
    address_sha256_ripemd160 = hashlib.new('ripemd160', bytes.fromhex(address_sha256)).hexdigest()
    address_sha256_ripemd160_00 = '00' + address_sha256_ripemd160
    address_sha256_ripemd160_00_base58check = b58encode_check(bytes.fromhex(address_sha256_ripemd160_00)).decode("utf-8")
    print(f'Bitcoin address (compressed): {address_sha256_ripemd160_00_base58check}')


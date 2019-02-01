import getpass
import hashlib

MAX_LEN = 447

# https://gist.github.com/curlysemi/b89576a6745583f077d870ea90b5da61
BLOCK_SIZE = 512
def gen_padding(len_message):
    num_blocks, remaining_bits = divmod(len_message, BLOCK_SIZE)
    num_blocks = num_blocks + 1
    num_zeros  = 0
    # 447 = 512 - 64 (the appended length) - 1 (the starting 1)
    if remaining_bits > 447:
        num_blocks = num_blocks + 1
        num_zeros  = (BLOCK_SIZE - remaining_bits) + 447
    else:
        num_zeros  = 447 - remaining_bits
    padding = "1" + ("0" * num_zeros) + '{:064b}'.format(len_message)
    assert((len(padding) + len_message) % BLOCK_SIZE == 0)
    return num_blocks, padding


def splitUint256(hex_string):
    hex_string = hex_string.replace('0x','')
    hex_string = hex_string.zfill(64)
    return int(hex_string[0:32], 16), int(hex_string[32:], 16)


def main():
    pw = getpass.getpass()
    pw = pw.strip()
    b = bytearray()
    b.extend(pw)
    l = len(b) * 8
    if l > MAX_LEN:
        raise Exception("Password is too long!")
    num_blocks, padding = gen_padding(l)
    bits = ''.join(format(byte, '08b') for byte in b)
    block = bits + padding
    parts = []
    parts.append(int(block[0:128], 2))
    parts.append(int(block[128:256], 2))
    parts.append(int(block[256:384], 2))
    parts.append(int(block[384:512], 2))
    h = hashlib.sha256(b).hexdigest()
    h0, h1 = splitUint256(h)
    parts.append(h0)
    parts.append(h1)
    parts = [str(n) for n in parts]

    print ' '.join(parts)

main()
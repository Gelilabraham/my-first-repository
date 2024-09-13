'''import string
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]
flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key)==1
b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)'''
'''
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))  # Convert char to 8-bit binary
        enc += ALPHABET[int(binary[:4], 2)]  # First 4 bits
        enc += ALPHABET[int(binary[4:], 2)]  # Last 4 bits
    return enc

def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET  # Convert character to index (0-15)
    t2 = ord(k) - LOWERCASE_OFFSET  # Convert key character to index (0-15)
    return ALPHABET[(t1 + t2) % len(ALPHABET)]  # Perform the shift within the bounds of ALPHABET

flag = "redacted"  # Ensure flag only has characters from 'a' to 'p'
key = "r"          # The key should be 1 character based on the assertion

# Check that the key only has characters in the allowed ALPHABET
assert all([k in ALPHABET for k in key])
assert len(key) == 1  # Ensure key is 1 character

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
    enc += shift(c, key[i % len(key)])

print(enc)'''

import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase  # Full alphabet

def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))  # Convert char to 8-bit binary
        enc += ALPHABET[int(binary[:4], 2)]  # First 4 bits
        enc += ALPHABET[int(binary[4:], 2)]  # Last 4 bits
    return enc

def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET  # Convert character to index
    t2 = ord(k) - LOWERCASE_OFFSET  # Convert key character to index
    return ALPHABET[(t1 + t2) % len(ALPHABET)]  # Perform the shift within the bounds of ALPHABET

flag = "yourflaghere"  # Your flag should match the range of allowed characters in ALPHABET
key = "yourkeyhere"    # Ensure the key only contains characters from ALPHABET

# Check that all characters in the key are in ALPHABET
assert all([k in ALPHABET for k in key])
assert len(key) >= 1  # Ensure the key has at least one character

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
    enc += shift(c, key[i % len(key)])

print(enc)

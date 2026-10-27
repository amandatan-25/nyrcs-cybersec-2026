ciphertext_hex = "PASTE_CIPHERTEXT_HEX_HERE"
ciphertext = bytearray.fromhex(ciphertext_hex)

# Known plaintext: b"role=user;..."
# "user" starts at byte index 5; change it to "root".
original = b"user"
desired = b"root"
start = 5

for i in range(len(original)):
    ciphertext[start + i] ^= original[i] ^ desired[i] # core formula

print("Modified ciphertext (hex):", ciphertext.hex())

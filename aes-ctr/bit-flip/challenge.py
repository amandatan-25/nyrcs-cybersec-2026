from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

KEY = get_random_bytes(16)
NONCE = get_random_bytes(8)
PLAINTEXT = b"role=user;uid=1001;access=basic"

def encrypt_message():
    return AES.new(KEY, AES.MODE_CTR, nonce=NONCE).encrypt(PLAINTEXT)

def main():
    ciphertext = encrypt_message()
    print("=== AES-CTR Role Modification ===")
    print("Goal: modify role=user to role=root.")
    print("Ciphertext (hex):", ciphertext.hex())
    modified_hex = input("Modified ciphertext (hex): ").strip()

    try:
        modified = bytes.fromhex(modified_hex)
    except ValueError:
        print("Invalid hex.")
        return
    if len(modified) != len(ciphertext):
        print("Wrong ciphertext length.")
        return

    plaintext = AES.new(KEY, AES.MODE_CTR, nonce=NONCE).decrypt(modified)
    print("Decrypted message:", plaintext.decode("ascii", errors="replace"))
    if plaintext.startswith(b"role=root;"):
        print("Correct!")
    else:
        print("Nope. Wrong ciphertext.")

if __name__ == "__main__":
    main()

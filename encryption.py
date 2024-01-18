from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(s):
    return (s + (16 - len(s) % 16) * chr(16 - len(s) % 16))

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def encrypt(text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.encrypt(pad(text).encode())

def decrypt(cipher_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(cipher_text))

key = get_random_bytes(16)

encrypted = encrypt("This is a secret message", key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)
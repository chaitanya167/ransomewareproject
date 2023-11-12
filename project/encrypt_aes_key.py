import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def generate_aes_key():
    return os.urandom(32)  # 256-bit key

def encrypt_file(file_path, aes_key):
    with open(file_path, 'rb') as f:
        data = f.read()

    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(b'\x00' * 16), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    with open(file_path, 'wb') as f:
        f.write(encrypted_data)

def main():
    # Define the path to the folder to be encrypted
    folder_to_encrypt = "/home/sec-lab/Dummy"

    # Generate an AES key for folder encryption
    aes_key = generate_aes_key()

    # Save the AES key to a file
    with open('aes_key.bin', 'wb') as key_file:
        key_file.write(aes_key)

    # Encrypt each file in the folder
    for root, dirs, files in os.walk(folder_to_encrypt):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, aes_key)

    print("Folder encrypted successfully.")

if __name__ == "__main__":
    main()

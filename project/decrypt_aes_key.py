import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes  # Ensure 'hashes' is correctly imported
from getpass import getpass

def decrypt_folder(folder_path, aes_key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                encrypted_data = f.read()

            cipher = Cipher(algorithms.AES(aes_key), modes.CFB(b'\x00' * 16), default_backend())
            decryptor = cipher.decryptor()
            decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

            with open(file_path, 'wb') as f:
                f.write(decrypted_data)

def main():
    # Define the path to the folder to be decrypted
    folder_to_decrypt = "/home/sec-lab/Dummy"

    # Load the AES key
    with open('aes_key.bin', 'rb') as key_file:
        aes_key = key_file.read()

    # Decrypt each file in the folder
    decrypt_folder(folder_to_decrypt, aes_key)

    print("Folder decrypted and unlocked successfully.")

if __name__ == "__main__":
    main()
